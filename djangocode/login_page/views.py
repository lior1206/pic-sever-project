from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_upload')
        else:
            messages.error(request, "There was an error logging in, please try again")
            return redirect('home')
    else:
        return render(request, 'registration/index.html', {})

@login_required
def user_upload(request):
    if request.method == "POST" and request.FILES.get('photo'):
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        uploaded_file_url = fs.url(filename)
        # Save the uploaded file URL or filename to the user's profile or another model if needed
        messages.success(request, f"Photo uploaded successfully: {uploaded_file_url}")
        return redirect('user_upload')
    return render(request, 'upload.html')
