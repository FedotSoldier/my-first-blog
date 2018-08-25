from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
	path('', views.post_list, name='post_list'),
	url(r'^post/(?P<pkey>\d+)/$', 
		views.post_detail, 
		name='post_detaill'),
	path('post/new/', views.post_new, name='post_new'),
	url(r'^post/(?P<pkey>\d+)/edittt/$', 
		views.post_edit, 
		name='post_edit'),
]

# Добавить кнопки домой в разных частях
# Добавить удаление поста