# api/views.py
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

# Task 1 list view (still open to all)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Task 2 CRUD ViewSet with permission classes
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    Explanation:
    - Anyone can GET (read) the list of books or a single book.
    - Only authenticated users can POST, PUT, DELETE.
    """
