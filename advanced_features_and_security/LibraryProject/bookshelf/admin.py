# LibraryProject/bookshelf/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Make sure this is your custom user model

class CustomUserAdmin(UserAdmin):
    # Add any customizations here if needed
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# Register the custom user model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)

