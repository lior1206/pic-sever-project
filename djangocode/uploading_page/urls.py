from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_upload/<str:username>/', views.user_upload, name='user_upload'),
]

