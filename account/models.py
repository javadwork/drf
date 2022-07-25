from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    show_site = models.BooleanField(default=False)
