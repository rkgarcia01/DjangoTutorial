# blog/models.py
from django.db import models
from django.urls import reverse

# To help us build new database models which will "model" thet characteristics of the data in our database, we import a module called "models" from django.db library


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


# <link rel="stylesheet" href="{% static 'css/base.css' %}">
# <link href="{% static 'css/base.css' %}" rel="stylesheet">
