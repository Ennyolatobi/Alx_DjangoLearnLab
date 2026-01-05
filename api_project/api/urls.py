from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router for CRUD endpoints
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Task 1 list view
    path('books/', BookList.as_view(), name='book-list'),

    # Task 2 CRUD endpoints (router handles GET, POST, PUT, DELETE)
    path('', include(router.urls)),
]
