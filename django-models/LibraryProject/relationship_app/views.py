from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView

# Function-Based View: List all books
def list_books_view(request):
    """List all books in the database."""
    books = Book.objects.all()  # Query all books
    return render(request, 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'