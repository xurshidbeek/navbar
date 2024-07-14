from django.shortcuts import render
from .models import UserProfile
from navbar.models import Books

def akk(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    if user_profile:
        books = Books.objects.all()

        return render(request, 'akk.html', {
            'purchased_books': books
        })
    else:
        # Handle case where there is no profile
        return render(request, 'akk.html', {
            'purchased_books': [],
            'wishlist_books': []
        })
