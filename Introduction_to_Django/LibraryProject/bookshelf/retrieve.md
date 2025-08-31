# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.get(id=1)   # or use the id you saw in shell
print(book.title, book.author, book.publication_year)
# Expected output: 1984 George Orwell 1949
