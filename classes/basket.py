from datetime import datetime

class Basket:
    def __init__(self, user_id, user_name, book_id, book_title, basket_date=None):
        self.user_id = user_id
        self.user_name = user_name
        self.book_id = book_id
        self.book_title = book_title
        self.basket_date = basket_date or datetime.now()
        

    def __str__(self):
        return f"|| Vartotojo kortelės numeris: {self.book_id} --> vardas, pavardė: {self.user_name}, paimta knyga: {self.book_title} --> paimė {self.basket_date.strftime("%Y-%m-%d")} ||"