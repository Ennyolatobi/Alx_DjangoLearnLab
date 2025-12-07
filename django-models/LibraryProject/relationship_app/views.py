from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Book, Library


# FUNCTION-BASED VIEW – List all books
def list_books_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# CLASS-BASED VIEW – Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# LOGIN VIEW
def login_view(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # redirect anywhere you want

    return render(request, 'relationship_app/login.html', {'form': form})


# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


# REGISTER VIEW
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto login after registering
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})
