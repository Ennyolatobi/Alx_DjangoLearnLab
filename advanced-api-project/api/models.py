from django.db import models

# Author model represents a book author.
# Each author can have multiple books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents a book written by an author.
# Each book belongs to one author.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship:
    # One Author -> Many Books
    author = models.ForeignKey(
        Author,
        related_name='books',  # allows author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
