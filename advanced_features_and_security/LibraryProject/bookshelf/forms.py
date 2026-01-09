from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm demonstrates secure handling of user input
    using Django forms to prevent SQL injection and XSS attacks.
    """

    class Meta:
        model = Book
        fields = ['title']
