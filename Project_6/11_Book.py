# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to 
# increase the count when a new book is added.

class Book:
    total_books = 0
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

#____________________________ Example usage
b1 = Book("Book1")
b2 = Book("Book2")
print(f"Total books: {Book.total_books}")