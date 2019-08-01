from django.urls import path

from . import views
app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogposts, name='blogposts'),
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]
