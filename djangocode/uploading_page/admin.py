from django.contrib import admin
from .models import UploadedPhoto
# Register your models here.
from django import forms

class PhotoUploadForm(forms.Form):
    photo = forms.ImageField()
    

admin.site.register(UploadedPhoto)