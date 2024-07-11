from django.urls import path, include
from .views import login_view, register_view, logout_view

urlpatterns = [
 path('log/', login_view, name='login'),
 path('reg/', register_view, name='register'),
 path('out/', logout_view, name='logout'),

]

