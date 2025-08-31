# Update

Command (in Django shell):
```python
book = Book.objects.get(id=1)   # or use the book variable if still in memory
book.title = "Nineteen Eighty-Four"
book.save()
book
```

# Expected output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
