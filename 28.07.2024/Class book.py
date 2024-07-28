class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")
book = Book("1984", "George Orwell", "1234567890")
book.display()
