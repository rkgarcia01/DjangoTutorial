# blog/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# ListView() --> A page representing a list of objects.


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
