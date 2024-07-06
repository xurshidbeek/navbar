from django.contrib import admin
from .models import Authors,Books

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'created_d')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('created_d',)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'description', 'author', 'price', 'count', 'created_d')
    list_display_links = ('id', 'tittle', 'description', 'author', 'price', 'count', 'created_d')
# Register your models here.

