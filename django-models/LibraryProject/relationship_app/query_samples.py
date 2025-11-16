import os
import django

# Set your Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ------------------------
# QUERY FUNCTIONS
# ------------------------

def query_books_by_author(author_name):
    """Query all books by a specific author name."""
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f"No author named '{author_name}' found.")
        return []

    books = list(author.books.all())
    print(f"Books by {author.name}: {[b.title for b in books]}")
    return books

def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library named '{library_name}' found.")
        return []

    books = list(library.books.all())
    print(f"Books in {library.name}: {[b.title for b in books]}")
    return books

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library using the OneToOne relationship."""
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library named '{library_name}' found.")
        return None

    librarian = getattr(library, 'librarian', None)
    if librarian is None:
        print(f"No librarian assigned for library '{library.name}'.")
    else:
        print(f"Librarian for {library.name}: {librarian.name}")
    return librarian

# ------------------------
# RUN EXAMPLES
# ------------------------

if __name__ == '__main__':
    print("=== Query all books by author 'Chinua Achebe' ===")
    query_books_by_author('Chinua Achebe')

    print("\n=== List all books in library 'Ife Public Library' ===")
    list_books_in_library('Ife Public Library')

    print("\n=== Retrieve librarian for library 'Ife Public Library' ===")
    retrieve_librarian_for_library('Ife Public Library')
