from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UploadedPhoto
from .forms import PhotoUploadForm

def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_upload')  # Simplified: no need to pass the username
        else:
            messages.error(request, "There was an error logging in, please try again.")
            return redirect('home')
    else:
        return render(request, 'registration/index.html')

@login_required
def user_upload(request):
    user = request.user  # Accessing the current logged-in user directly
    if request.method == "POST":
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_photo = form.save(commit=False)
            uploaded_photo.user = user  # Assign the logged-in user to the uploaded photo
            uploaded_photo.save()
            messages.success(request, "Photo uploaded successfully!")
            return redirect('user_upload')  # No need to pass the username
        else:
            messages.error(request, "Failed to upload photo. Please try again.")
    else:
        form = PhotoUploadForm()

    user_photos = UploadedPhoto.objects.filter(user=user)
    return render(request, 'upload.html', {'user_photos': user_photos, 'form': form})
