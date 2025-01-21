from django.urls import path
from . import views

urlpatterns = [
    # After login, the user is redirected to this upload page
    path('', views.user_upload, name='user_upload'),  # User upload page
]
