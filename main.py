import functions.login_functions as fl
import functions.menu_functions as fm

def main():
    fl.create_initial_fakeadmin()

    print("\n======= Bibliotekos sistema =======\n")
    username = input("Įveskite kortelės numerį: ")
    password = input("Įveskite slaptažodį: ")

    user = fl.login(username, password)
    if user:
        print(f"\nSveiki, {user.user_name}! Jūsų rolė: {user.user_role}")
        print("-" * 70)
        if user.user_role == "bibliotekininkas":
            fm.librarian_menu()
        else:
            fm.reader_menu(user)
    else:
        print("Neteisingas kortelės numeris arba slaptažodis.")

main()


    