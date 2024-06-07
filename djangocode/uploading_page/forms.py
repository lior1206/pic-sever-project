from django import forms
from .models import UploadedPhoto
#this file job is to connect the db model to the views.py file and point the corect colume.
class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedPhoto
        fields = ['photo']
