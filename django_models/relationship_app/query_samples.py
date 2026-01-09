from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author
    author = Author.objects.first()  # Example: first author
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # 2. List all books in a library
    library = Library.objects.first()  # Example: first library
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

    # 3. Retrieve the librarian for a library
    librarian = library.librarian  # OneToOne relationship
    print(f"Librarian for {library.name}: {librarian.name}")

# Run sample queries
if __name__ == "__main__":
    run_queries()
