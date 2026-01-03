from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Blog Post model
    - title: The title of the blog post
    - content: The main content of the post
    - published_date: Automatically set when created
    - author: Link to Django's built-in User model
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
