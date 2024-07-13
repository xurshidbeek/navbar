from django.urls import path
from .views import akk

urlpatterns = [
    path('akk/', akk , name='akk'),
]
