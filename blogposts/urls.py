from django.conf.urls import url
from django.urls import path, include
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    path('', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    path('new/', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
]