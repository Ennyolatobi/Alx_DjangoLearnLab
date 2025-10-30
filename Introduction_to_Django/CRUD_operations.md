Django Model CRUD Operations Book Model

This document demonstrates basic CRUD (Create, Retrieve, Update, Delete) operations using Django’s ORM through the Django shell.
All operations were performed on the Book model within the bookshelf app.

🟢 CREATE

Command:

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book


Output:

<Book: 1984>


Explanation:
This command creates a new Book instance with the given title, author, and publication year.
Django automatically saves the record into the connected database.

🔵 RETRIEVE

Command:

from bookshelf.models import Book
Book.objects.all()


Output:

<QuerySet [<Book: 1984>]>


Explanation:
This retrieves all book records currently stored in the database.
It shows one record the book we just created.

🟠 UPDATE

Command:

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book


Output:

<Book: Nineteen Eighty-Four>


Explanation:
This command retrieves the book titled “1984,” updates its title to “Nineteen Eighty-Four,” and saves the changes.
The updated title is now reflected in the database.

🔴 DELETE

Command:

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()


Output:

(1, {'bookshelf.Book': 1})
<QuerySet []>


Explanation:
This command deletes the book record from the database.
The tuple shows that one record was deleted, and the empty QuerySet confirms that no books remain.
