from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import os

class CustomUserManager(BaseUserManager):
    """Custom user manager for creating users with additional fields."""
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Create and save a regular user with email and password.
        Handles date_of_birth and profile_photo fields.
        """
        if not username:
            raise ValueError(_('The Username field must be set'))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Create and save a SuperUser with admin permissions.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    date_of_birth = models.DateField(
        null=True, 
        blank=True, 
        verbose_name=_("Date of Birth")
    )
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        null=True,
        blank=True,
        verbose_name=_("Profile Photo")
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Book(models.Model):
    """Book model with custom permissions."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    created_by = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='created_books'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_view_book", "Can view book details"),
            ("can_create_book", "Can create book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"


class BookCategory(models.Model):
    """Simple category model."""
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
