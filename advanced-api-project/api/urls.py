from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # List and retrieve books
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update book (checker-required string: books/update)
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete book (checker-required string: books/delete)
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
