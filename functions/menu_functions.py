import streamlit as st
from . import librarian_functions as lf
from . import book_function as bf
from . import reader_functions as rf


def librarian_menu():
    st.subheader("Bibliotekininko meniu")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Vartotojų valdymas", key="user_management_btn"):
            st.session_state.current_menu = "user_management"
    with col2:
        if st.button("Knygų valdymas", key="book_management_btn"):
            st.session_state.current_menu = "book_management"
    
    if st.button("Atsijungti", key="logout_librarian"):
        st.session_state.clear()
        st.experimental_rerun()

    if "current_menu" in st.session_state:
        if st.session_state.current_menu == "user_management":
            user_management_menu()
        elif st.session_state.current_menu == "book_management":
            book_management_menu()


def user_management_menu():
    st.subheader("Vartotojų valdymas")
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Sukurti vartotoją", key="create_user_btn"):
            lf.create_user()
    with col2:
        if st.button("Ištrinti vartotoją", key="delete_user_btn"):
            lf.delete_user()
    with col3:
        if st.button("Atnaujinti vartotoją", key="update_user_btn"):
            lf.update_user()
    with col4:
        if st.button("Peržiūrėti vartotojų sąrašą", key="list_users_btn"):
            lf.list_users()
    
    if st.button("Grįžti į pradinį meniu", key="back_to_librarian_menu_users"):
        st.session_state.current_menu = "librarian_main"
        st.experimental_rerun()


def book_management_menu():
    st.subheader("Knygų valdymas")

    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns(2)

    with col1:
        if st.button("Pridėti knygą", key="add_book_btn"):
            bf.add_book()
    with col2:
        if st.button("Ištrinti knygą", key="delete_book_btn"):
            bf.delete_book()
    with col3:
        if st.button("Atnaujinti knygą", key="update_book_btn"):
            bf.update_book()
    with col4:
        if st.button("Peržiūrėti visas knygas", key="list_all_books_btn"):
            bf.list_books()
    with col5:
        if st.button("Ieškoti knygos pagal pavadinimą/autorių", key="search_book_btn"):
            bf.search_books()

    if st.button("Grįžti į pradinį meniu", key="back_to_librarian_menu_books"):
        st.session_state.current_menu = "librarian_main"
        st.experimental_rerun()


def reader_menu(user):
    st.subheader(f"Sveiki, {user.user_name}! Skaitytojo meniu")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Peržiūrėti visas knygas", key="reader_list_books_btn"):
            rf.list_books() # Assuming you'll adapt bf.list_books() to reader_functions or pass it.
    with col2:
        if st.button("Paimti knygą", key="take_book_btn"):
            rf.book_basket(user)
    with col3:
        if st.button("Grąžinti knygą", key="return_book_btn"):
            rf.return_book(user)
    with col4:
        if st.button("Mano pasiskolintos knygos", key="my_borrowed_books_btn"):
            rf.view_my_books(user)
            
    if st.button("Atsijungti", key="logout_reader"):
        st.session_state.clear()
        st.experimental_rerun()