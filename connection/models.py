from django.db import models

# Create your models here.


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
