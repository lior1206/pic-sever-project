# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UploadedPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.photo.name}"
