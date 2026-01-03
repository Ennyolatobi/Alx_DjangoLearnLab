from rest_framework import serializers
from datetime import date
from .models import Author, Book


# BookSerializer handles serialization of Book model
# and includes custom validation for publication year.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to prevent future publication years
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# AuthorSerializer serializes Author model
# and includes a nested BookSerializer to show related books.
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer for books written by the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
