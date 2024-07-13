from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from navbar.models import Books

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_books = models.ManyToManyField(Book, related_name='purchased_by', blank=True)
    wishlist_books = models.ManyToManyField(Book, related_name='wishlist_by', blank=True)

    def __str__(self):
        return self.user.username
