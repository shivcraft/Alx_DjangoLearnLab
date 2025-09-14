# advanced_features_and_security

Model: Article
Permissions:
 - can_view
 - can_create
 - can_edit
 - can_delete

Groups:
 - Viewers -> can_view
 - Editors -> can_view, can_create, can_edit
 - Admins -> can_view, can_create, can_edit, can_delete

How to use:
1. Run migrations: python manage.py makemigrations && python manage.py migrate
2. Create superuser: python manage.py createsuperuser
3. Start server: python manage.py runserver
4. Configure groups and assign users via /admin
