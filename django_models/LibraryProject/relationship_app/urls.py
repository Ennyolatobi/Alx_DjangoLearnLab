# File: relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Function-based view
    path('books/', views.list_books, name='list_books'),

    # Class-based view (expects library id as PK)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
