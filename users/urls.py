from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import login, register

urlpatterns = ([
    path('login/', login, name='login'),
    path('reg/', register, name='register')
]




 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))



