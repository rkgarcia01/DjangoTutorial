from django.contrib import admin

# Register your models here for them to show on Django admin.
from .models import Post

admin.site.register(Post)
