from django.contrib import admin
from .models import UploadedPhoto
from django import forms
#this file job is to give the super users the filds to control in the /admin control page .
class PhotoUploadForm(forms.Form):
    photo = forms.ImageField()
    

admin.site.register(UploadedPhoto)