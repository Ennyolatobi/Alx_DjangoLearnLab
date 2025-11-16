from django.urls import path
from .views import list_books_view, LibraryDetailView

urlpatterns = [
    path('books/', list_books_view, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
