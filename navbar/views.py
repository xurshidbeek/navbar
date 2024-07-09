from django.shortcuts import render
from .models import Books, Authors


def home(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Books.objects.filter(tittle__icontains=search)|Books.objects.filter(author__first_name__icontains=search)
        if books:
            return render(request, 'book.html', {'book': books, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'book.html', {'message': "NOt found"})
    return render(request, 'home.html')


def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Books.objects.filter(tittle__icontains=search)|Books.objects.filter(author__first_name__icontains=search)
        if books:
            return render(request, 'book.html', {'book': books, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'book.html', {'message': "NOt found"})
    book = Books.objects.all()
    context = {'book': book}
    return render(request, 'book.html', context=context)


def author(request):
    author = Authors.objects.all()
    context = {'author':author}
    return render(request, 'author.html', context=context)


def book_detail(request, id):
    if request.method == 'POST':
        search = request.POST['search']
        books = Books.objects.filter(tittle__icontains=search) | Books.objects.filter(
            author__first_name__icontains=search)
        if books:
            return render(request, 'book.html', {'book': books, "value": search, "message": "Succesfuly"})
        else:
            return render(request, 'book.html', {'message': "NOt found"})
    book = Books.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})
