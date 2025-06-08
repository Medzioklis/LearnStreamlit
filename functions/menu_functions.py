from . import librarian_functions as lf
from . import book_function as bf
from . import reader_functions as rf


def librarian_menu():
    while True:
        print("\n===== Bibliotekininko meniu =====\n")
        print("1. Vartotojų valdymas")
        print("2. Knygų valdymas")
        print("0. Atsijungti")
       
        choice = int(input("Pasirinkite: "))

        match choice:
            case 1:
                user_management_menu()  
            case 2:
                book_management_menu()
            case 0:
                print("Atsijungėte")
                exit()
            case _:
                print("Neteisingas pasirinkimas.")


def user_management_menu():
    while True:
        print("\n======= Vartotojų valdymas =======\n")
        print("1. Sukurti vartotoją")
        print("2. Ištrinti vartotoją")
        print("3. Atnaujinti vartotoją")
        print("4. Peržiūrėti vartotojų sąrašą")
        print("0. Grįžti į pradinį meniu")
        
        choice = int(input("Pasirinkite: "))

        match choice:
            case 1:
                lf.create_user()
            case 2:
                lf.delete_user()
            case 3:
                lf.update_user()
            case 4:
                lf.list_users()
            case 0:
                librarian_menu()
            case _:
                print("Neteisingas pasirinkimas.")


def book_management_menu():
    while True:
        print("\n=========== Knygų valdymas ===========\n")
        print("1. Pridėti knygą")
        print("2. Ištrinti knygą")
        print("3. Atnaujinti knygą")
        print("4. Peržiūrėti visas knygas")
        print("5. Ieškoti knygos pagal pavadinimą/autorių")
        print("0. Grįžti į pradinį meniu")
        
        choice = int(input("Pasirinkite: "))

        match choice:
            case 1:
                bf.add_book()
            case 2:
                bf.delete_book()
            case 3:
                bf.update_book()
            case 4:
                bf.list_books()
            case 5:
                bf.search_books()
            case 0:
                librarian_menu()
            case _:
                print("Neteisingas pasirinkimas.")


def reader_menu(user):
    while True:
        print("\n=== Skaitytojo meniu ===\n")
        print("1. Peržiūrėti visas knygas")
        print("2. Paimti knygą")
        print("3. Grąžinti knygą")
        print("4. Mano pasiskolintos knygos")
        print("0. Atsijungti")
        
        choice = int(input("Pasirinkite: "))

        match choice:

            case 1:
                bf.list_books()
            case 2:
                rf.book_basket(user)
            case 3:
                rf.return_book(user)
            case 4:
                rf.view_my_books(user)
            case 0:
                print("Atsijungėte")
                exit()
            case _:
                print("Neteisingas pasirinkimas.")