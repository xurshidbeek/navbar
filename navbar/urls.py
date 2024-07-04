from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home, books, author

urlpatterns = [
    path('', home, name='home'),
    path('book/', books, name='books'),
    path('auth/', author, name='author'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)