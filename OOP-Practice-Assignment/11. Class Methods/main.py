#Assignment No-11:
#Create a class Book with a class variable total_books. 
#Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        return cls.total_books
    
book1 = Book("Power of Habit")
book2 = Book("Intelligent Investor")
book3 = Book("Design Patterns")

print(Book.total_books)