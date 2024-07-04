from django.shortcuts import render
from .models import Books, Authors


def home(request):
    return render(request, 'home.html')


def books(request):
    book = Books.objects.all()
    context = {'book': book}
    return render(request, 'book.html', context=context)


def author(request):
    authors = Authors.objects.all()
    context = {'author':authors}
    return render(request, 'author.html', context=context)

def book_list(request):
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(title__icontains=query)
    else:
        books = Books.objects.all()
    return render(request, 'book.html', {'books': books})
# Create your views here.
