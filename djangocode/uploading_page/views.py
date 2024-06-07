from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UploadedPhoto
from .forms import PhotoUploadForm

def home(request):#this function belongs to the loging page it uses requests to get the username and password and to authenticate them it uses django bulit-in authenticating option.
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if request.method == "POST":
                login(request, user)
            return redirect('user_upload', username=user.username)#if the user passed the authenticating process this line sands him to the uploadig page by using the redirect func that we imported from django.
        else:
            messages.error(request, "There was an error logging in, please try again.")
            return redirect('home')
    else:
        return render(request, 'registration/index.html')

@login_required
def user_upload(request, username):
    user = request.user 
    if request.method == "POST":
        form = PhotoUploadForm(request.POST, request.FILES)#uses the form file in order to connect the db model to the app 
        if form.is_valid():
            uploaded_photo = form.save(commit=False)# the following lines are a standart way off uploading files in django and implenting the metadata in the db model. 
            uploaded_photo.user = user  
            uploaded_photo.save()
            messages.success(request, "Photo uploaded successfully!")
            return redirect('user_upload', username=user.username)
        else:
            messages.error(request, "Failed to upload photo. Please try again.")
    else:
        form = PhotoUploadForm()

    user_photos = UploadedPhoto.objects.filter(user=user)
    return render(request, 'upload.html', {'user_photos': user_photos, 'form': form, 'username': user.username})
