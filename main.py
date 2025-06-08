import streamlit as st                                                       #
import functions.login_functions as fl
import functions.menu_functions as fm

def main():
    fl.create_initial_fakeadmin()

    st.title("Bibliotekos sistema")                                          #

    username = st.text_input("Įveskite kortelės numerį:")
    password = st.text_input("Įveskite slaptažodį: ", type = "password")

    if st.button("Prisijungti"):
        user = fl.login(username, password)
        if user:
            st.success(f"\nSveiki, {user.user_name}! Jūsų rolė: {user.user_role}")
        
        if user.user_role == "bibliotekininkas":
            fm.librarian_menu()
        else:
            fm.reader_menu(user)
    else:
        st.error("Neteisingas kortelės numeris arba slaptažodis.")

main()


    