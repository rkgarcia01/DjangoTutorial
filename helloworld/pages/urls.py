from django.urls import path

# from .views import homePageViewd
# By referring to the view.py file as .view we are telling Django to look within the current directory for a view.py file and import the CBV, FBV, or GCBV
from .views import HomePageView, AboutPageView

# we use .as_view() when useing a Class-Based View in 'views.py'
urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    # path("", homePageView, name="home"),
]
