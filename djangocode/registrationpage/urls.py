from django.urls import path
from . import views

urlpatterns = [
    # Registration page URL
    path('', views.register, name='register'),  # Registration page
]
