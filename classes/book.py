class Book:
    def __init__(self, book_id, book_title, book_author, book_genre, book_release, book_unit):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_genre = book_genre
        self.book_release = book_release
        self.book_unit = book_unit 
    
    def __str__(self):
        return (f"ID: {self.book_id}, Knygos pavadinimas: {self.book_title}, autorius: {self.book_author}, žanras: {self.book_genre}, išleidimo metai: {self.book_release}, sandelyje: {self.book_unit} vnt.")