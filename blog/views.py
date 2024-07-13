from django.shortcuts import render
from .models import UserProfile

def akk(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    if user_profile:
        olingan = user_profile.purchased_books.all()
        olmoqchi = user_profile.wishlist_books.all()
        return render(request, 'akk.html', {
            'purchased_books': olingan,
            'wishlist_books': olmoqchi,
        })
    else:
        # Handle case where there is no profile
        return render(request, 'akk.html', {
            'purchased_books': [],
            'wishlist_books': []
        })
