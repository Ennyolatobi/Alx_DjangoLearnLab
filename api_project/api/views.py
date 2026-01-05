from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing Task 1 ListAPIView
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Task 2: CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD operations for the Book model:
    list, retrieve, create, update, delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
