from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
	path('', views.post_list, name='post_list'),
	url(r'^post/(?P<pkey>\d+)/$', 
		views.post_detail, 
		name='post_detaill'),
	path('post/new/', views.post_new, name='post_new'),
	url(r'^post/(?P<pkey>\d+)/edit/$', 
		views.post_edit, 
		name='post_edit'),
	path('drafts/',views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', 
		views.post_publish, 
		name='post_publish'),
	url(r'^post/(?P<pkey>\d+)/remove/$', 
		views.post_remove, 
		name='post_remove'),

]

# Добавить кнопки домой в разных частях
# Добавить удаление поста