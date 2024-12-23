from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# ListView() --> A page representing a list of objects.


class BlogListView(ListView):
    model = Post
    template_name = "home.html"
