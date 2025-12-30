# Advanced Features & Security

## Custom User Model
- Extends `AbstractUser` with `date_of_birth` and `profile_photo`
- Custom manager handles user creation
- `AUTH_USER_MODEL = 'bookshelf.CustomUser'`

## Permissions & Groups
- Custom permissions: `can_view_book`, `can_create_book`, `can_edit_book`, `can_delete_book`
- Groups: Viewers, Editors, Admins
- Views protected with `@permission_required`

## Security Features
- HTTPS enforcement: `SECURE_SSL_REDIRECT = True`
- HSTS enabled: `SECURE_HSTS_SECONDS = 31536000`
- Secure cookies: `SESSION_COOKIE_SECURE = True`
- CSRF protection in all forms
- CSP headers configured
- XSS filtering enabled

## Testing
1. Run `python manage.py runserver`
2. Test with different user groups via admin
3. Verify permission enforcement
