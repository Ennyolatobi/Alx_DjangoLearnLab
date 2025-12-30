from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.views import View
from .models import Book, BookCategory
from .forms import BookForm  # Assuming you have this form

@login_required
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    """Secure book list view with permission check."""
    query = request.GET.get('q')
    books = Book.objects.filter(created_by=request.user)
    
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    
    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'query': query
    })

@login_required
@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
    """Secure book creation with permission check."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})

@login_required
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    """Secure book editing with permission check."""
    book = get_object_or_404(Book, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookshelf/form_example.html', {'form': form})

@login_required
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    """Secure book deletion with permission check."""
    book = get_object_or_404(Book, pk=pk, created_by=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
