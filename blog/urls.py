from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list,name = 'post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.create_post,name='create_post'),
    path('post/<int:pk>/edit/',views.edit_post,name='edit_post')
]