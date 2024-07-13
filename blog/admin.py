from django.contrib import admin
from django.contrib import admin
from navbar.models import Books
from .models import UserProfile, Book

admin.site.register(Book)
admin.site.register(UserProfile)


# Register your models here.
