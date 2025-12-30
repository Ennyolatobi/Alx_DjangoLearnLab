from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, BookCategory

class CustomUserAdmin(UserAdmin):
    """Admin configuration for custom user model."""
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

# Register custom user admin
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin for Book model with permissions."""
    list_display = ['title', 'author', 'publication_date', 'created_by']
    list_filter = ['publication_date', 'created_by']
    search_fields = ['title', 'author', 'isbn']

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    """Admin for BookCategory."""
    list_display = ['name', 'created_by']
