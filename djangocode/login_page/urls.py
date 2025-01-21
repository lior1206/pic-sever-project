from django.urls import path
from . import views

urlpatterns = [
    # Custom login page URL
    path('', views.home, name='home'),  # Login page home view
]
