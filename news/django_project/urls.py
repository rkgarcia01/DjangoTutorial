"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

"""
We want to have our "home.html" template appear as the homepage, but we do not
want to build a dedicated "pages" app just yet. We can use the shortcut of importing
"TemplateView" and setting the "template_name" right in our url pattern.
"""

# path("accounts/", include("django.contrib.auth.urls")),
#  - This lines includes a set of 'predefined authentication URLs provided
#    authentication framework. these include
#   1. /accounts/login/ -> Handles user login (renders the login page)
#   2. /accounts/logout/ -> Handles user logout
#   3. /accounts/password_change/ -> Allows users to change passwords
#   4. /accounts/password_reset/ -> Provides password reset functionality.
#  - when a user visits '/accounts/login/', Django automatically uses the built-in
#    login view, even though you did not explicitly define it.
#  - Once it runs it, it renders the 'login.html' template.
#  - Authentication is performed using the built-in Authentication Form which you did not
#    have to create manually
#  - in 'views.py', using reverse_lazy it redirects 'home, or honmepage.
# path("", TemplateView.as_view(template_name="home.html"), name="home"),
#  - Once loged in, DJango looks at 'LOGIN_REDIRECT_URL' and since it is
#    LOGIN_REDIRECT_URL = "home", Django looks for the URL patter with the name "home"
#    this means it looks at "path("", TemplateView.as_view(template_name="home.html"), name="home"),"
#    and the user is redirected to '/' (the root URL), which serves 'home.html'.
#  - Note: likeise applies to logging out.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
