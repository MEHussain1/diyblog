from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),  # /blog/
    path('blogs/', views.blog_list, name='blog_list'),  # list of posts (paginated)
    path('bloggers/', views.blogger_list, name='blogger_list'),
    path('blogger/<int:pk>/', views.blogger_detail, name='blogger_detail'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/create/', views.create_comment, name='create_comment'),
    path('register/', views.register, name='register'),
    path('create_post/', views.create_post, name='create_post'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/blog/blogs/'), name='logout'),

]
