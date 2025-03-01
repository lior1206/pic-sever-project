from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#this page controls the app urls and pathes
urlpatterns = [
    path('', views.home, name='home'),
    path('user_upload/', views.user_upload, name='user_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
