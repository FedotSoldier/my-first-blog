from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(
		published_date__lte=timezone.now()
		).order_by('created_date') # ).order_by('published_date')

	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pkey): # мы должны использовать то же имя переменной, что мы выбрали для обработки URL (pkey)
	post = get_object_or_404(Post, pk=pkey)
	return render(request, 'blog/post_detail.html', {'post': post} )

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('post_detaill', pkey=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pkey):
	post = get_object_or_404(Post, pk=pkey)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('post_detaill', pkey=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(
		published_date__isnull=True
		).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detaill', pkey=pk)

@login_required
def post_remove(request, pkey):
	post=get_object_or_404(Post, pk=pkey)
	post.delete()
	return redirect('post_list')

@login_required
def add_comment_to_post(request, pkey):
	post = get_object_or_404(Post, pk=pkey)
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			#if request.user.is_authenticated :
			comment.author=request.user
			#else:
			#	comment.author='Anonimous'
			comment.post=post
			comment.save()
			return redirect('post_detaill', pkey=post.pk)
	else:
		form = CommentForm()
	return render(request, 'blog/add_comment_to_post.html', {'form': form})

# Здесь уже идет работа с бд Comment(pkey(pk) уже принадлежит этой бд)
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detaill', pkey=comment.post.pk)

@login_required
def comment_remove(request, pkey):
    comment = get_object_or_404(Comment, pk=pkey)
    comment.delete()
    return redirect('post_detaill', pkey=comment.post.pk)