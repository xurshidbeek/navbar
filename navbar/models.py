from django.db import models
from django.contrib.auth.models import User

class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    created_d = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.first_name} {self.last_name}"



class Books(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Authors,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="book/")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
    created_d = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.tittle


class Comments(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Books)
    created_d = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text