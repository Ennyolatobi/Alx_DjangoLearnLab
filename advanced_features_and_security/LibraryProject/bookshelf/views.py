from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Django ORM is used here to prevent SQL injection and ensure safe data access

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Using Django ORM instead of raw SQL for security
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # This view is protected by permissions to prevent unauthorized access
    return render(request, 'bookshelf/create_book.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Access restricted to users with edit permission
    return render(request, 'bookshelf/edit_book.html')


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Delete actions are protected to enhance application security
    return render(request, 'bookshelf/delete_book.html')
