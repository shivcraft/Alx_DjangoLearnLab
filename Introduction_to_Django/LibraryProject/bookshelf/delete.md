# Delete

Command (in Django shell):
```python
book = Book.objects.get(id=1)
book.delete()
Book.objects.all()
```

# Expected output:
# (1, {'bookshelf.Book': 1})   # deletion return
# <QuerySet []>               # no books remain
