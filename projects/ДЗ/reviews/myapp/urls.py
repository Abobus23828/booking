from django.urls import path
from myapp import views

urlpatterns = [
    path('rewiews/', views.reviews_list, name='review-list'),
    
]