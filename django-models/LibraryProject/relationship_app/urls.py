from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # User authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # Role-based access URLs
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),

    # Book views
    path('books/', views.list_books_view, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),                  # Add book
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),      # Edit book
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),# Delete book

    # Library detail view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
