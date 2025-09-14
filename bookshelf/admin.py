from django.contrib import admin
from .models import Book

# Customize how the Book model appears in the admin
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # show these columns in list view
    list_filter = ("publication_year", "author")            # filters on the right
    search_fields = ("title", "author")                     # search box

# Register the model + custom admin
admin.site.register(Book, BookAdmin)
