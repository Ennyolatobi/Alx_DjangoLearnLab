# File: relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library  # <-- Include Library here!

# ---------------- Function-based View ----------------
def list_books(request):
    """
    Function-based view to list all books in the database.
    """
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ---------------- Class-based View ----------------
class LibraryDetailView(DetailView):
    """
    Class-based view to display details of a specific library,
    including all books it contains.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_object(self):
        library_id = self.kwargs.get('pk')
        return get_object_or_404(Library, id=library_id)
