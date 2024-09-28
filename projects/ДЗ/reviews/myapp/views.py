from django.shortcuts import render
from .models import Reviews
# Create your views here.

def reviews_list():
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(reviews, '/index.html', context)