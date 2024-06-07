from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#this file is the way of django to deal with the data base  the lines down created the table that the photo metadata is going to be saved in.  
class UploadedPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.photo.name}"
