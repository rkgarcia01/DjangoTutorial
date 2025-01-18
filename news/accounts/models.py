# news/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# null - It is database-related. When a field has "null=True", it can store a dataabase entry as NULL, meaning no value
# blank = It is a validation-related. If bank=True when a form will allow an emtpy value, whereas if blank=False, then a value is required
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
