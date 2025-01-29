# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


# * TemplateView -> a class generic class-based view which means we only need to specify
#   our 'template_name' to use it.
