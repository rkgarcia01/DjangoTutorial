from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# capital HomePageView since it is class or Class-Based View(CBV)
class HomePageView(TemplateView):
    template_name = "home.html"


# capital HomePageView since it is class or Class-Based View(CBV)
class AboutPageView(TemplateView):
    template_name = "about.html"


# def homePageView(request):     # lowercase homePageView since it is a function
# return HttpResponse("Hello, World!")


# Create your views here.
