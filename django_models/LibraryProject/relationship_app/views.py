# from .models import Library

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    """
    Displays details for a specific library,
    listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_object(self):
        return get_object_or_404(Library, pk=self.kwargs.get('pk'))


def list_books(request):
    from .models import Book
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
