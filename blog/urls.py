from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, post, category, search_posts
from .forms import add_posts, UpdatePost


urlpatterns = [
    #site unchild
    path('',home),
    path('home/',home, name='home'),
    path('blog/<slug:url>',post, name='blog'),
    #path('blog/<int:pk>',post, name='blog'),
    path('category/<slug:url>',category, name='category'),
    path('search_posts',search_posts, name='search-posts'),
    path('add_posts/', add_posts.as_view(), name='add-posts'),
    path('blog/edit/<int:pk>',UpdatePost.as_view(), name='update-posts'),
] 
