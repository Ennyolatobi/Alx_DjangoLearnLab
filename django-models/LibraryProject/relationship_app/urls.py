from django.urls import path
from .views import login_view, logout_view, register_view
from .views import list_books_view, LibraryDetailView

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),

    # Existing views
    path("books/", list_books_view, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
