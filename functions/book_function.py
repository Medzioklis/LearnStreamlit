import streamlit as st
from classes.book import Book
from . import data_functions as df

def add_book():
    st.subheader("Pridėti knygą")
    books = df.load_books()

    with st.form("add_book_form", clear_on_submit=True):
        book_title = st.text_input("Įveskite knygos pavadinimą:")
        book_author = st.text_input("Įveskite autorių:")
        book_genre = st.selectbox(
            "Pasirinkite knygos žanrą:",
            ("romanas", "detektyvas", "fantastika", "biografija", "") # Add empty string for initial state if desired
        )
        book_release = st.text_input("Įveskite išleidimo metus:")
        book_unit = st.number_input("Įveskite kiekį (kiek egzempliorių):", min_value=0, step=1, value=0)
        
        submitted = st.form_submit_button("Pridėti knygą")

        if submitted:
            if book_title and book_author and book_genre and book_release and book_unit is not None:
                book_id = df.get_id() # Ensure get_id() generates unique IDs appropriately
                book = Book(book_id, book_title, book_author, book_genre, book_release, book_unit)
                books.append(book)
                df.save_books(books)
                st.success(f"Knyga **{book.book_title}** pridėta. ID: {book.book_id}, autorius: {book.book_author}, žanras: {book.book_genre}, išleidimo metai: {book.book_release}, sandėlyje: {book.book_unit} vnt.")
            else:
                st.error("Prašome užpildyti visus laukus.")

def delete_book():
    st.subheader("Ištrinti knygą")
    books = df.load_books()
    
    book_id_to_delete = st.text_input("Įveskite knygos ID, kurią norite ištrinti:")
    
    if st.button("Ištrinti knygą"):
        try:
            book_id_to_delete_int = int(book_id_to_delete)
            original_len = len(books)
            books = [book for book in books if int(book.book_id) != book_id_to_delete_int]
            
            if len(books) < original_len:
                df.save_books(books)
                st.success(f"Knyga su ID: **{book_id_to_delete}** ištrinta.")
            else:
                st.error(f"Knyga su ID: **{book_id_to_delete}** nerasta.")
        except ValueError:
            st.error("Netinkamas ID formatas. Įveskite skaičių.")


def update_book():
    st.subheader("Atnaujinti knygą")
    books = df.load_books()
    
    book_id_to_update = st.text_input("Įveskite knygos ID, kurią norite atnaujinti:")
    
    if book_id_to_update:
        found_book = None
        try:
            book_id_to_update_int = int(book_id_to_update)
            for book in books:
                if int(book.book_id) == book_id_to_update_int:
                    found_book = book
                    break
        except ValueError:
            st.error("Netinkamas ID formatas. Įveskite skaičių.")
            return
            
        if found_book:
            st.write(f"Atnaujinama knyga: **{found_book.book_title}** (ID: {found_book.book_id})")
            
            with st.form("update_book_form"):
                new_book_title = st.text_input("Naujas pavadinimas (palikite tuščią, jei nekeičiate):", value=found_book.book_title)
                new_book_author = st.text_input("Naujas autorius (palikite tuščią, jei nekeičiate):", value=found_book.book_author)
                
                genres = ["romanas", "detektyvas", "fantastika", "biografija"]
                current_genre_index = genres.index(found_book.book_genre) if found_book.book_genre in genres else 0
                new_book_genre = st.selectbox(f"Naujas žanras (dabar: {found_book.book_genre}):", genres, index=current_genre_index)
                
                new_book_release = st.text_input("Nauji išleidimo metai (palikite tuščią, jei nekeičiate):", value=found_book.book_release)
                new_book_unit = st.number_input(f"Atnaujinkite vnt. skaičių (dabar yra: {found_book.book_unit} vnt.):", min_value=0, step=1, value=found_book.book_unit)
                
                submitted = st.form_submit_button("Atnaujinti")
                
                if submitted:
                    if new_book_title:
                        found_book.book_title = new_book_title
                    if new_book_author:
                        found_book.book_author = new_book_author
                    found_book.book_genre = new_book_genre # Selectbox always returns a value
                    if new_book_release:
                        found_book.book_release = new_book_release
                    found_book.book_unit = new_book_unit # Number input always returns a value
                    
                    df.save_books(books)
                    st.success(f"Knyga **{found_book.book_title}** atnaujinta. ID: {found_book.book_id}, autorius: {found_book.book_author}, žanras: {found_book.book_genre}, išleidimo metai: {found_book.book_release}, sandėlyje: {found_book.book_unit} vnt.")
        else:
            st.error("Knyga nerasta.")


def search_books():
    st.subheader("Ieškoti knygos")
    books = df.load_books()
    
    search_input = st.text_input("Ieškokite pagal knygos pavadinimą arba autorių:").lower()
    
    if search_input:
        results = [book for book in books if search_input in book.book_title.lower() or search_input in book.book_author.lower()]
        
        if results:
            for book in results:
                st.markdown("---")
                st.write(f"**Pavadinimas:** {book.book_title}")
                st.write(f"**Autorius:** {book.book_author}")
                st.write(f"**Žanras:** {book.book_genre}")
                st.write(f"**Išleidimo metai:** {book.book_release}")
                st.write(f"**Prieinama:** {book.book_unit} vnt.")
            st.markdown("---")
        else:
            st.info("Knygų nerasta.")
    else:
        st.info("Įveskite paieškos terminą.")


def list_books():
    st.subheader("Visos knygos")
    books = df.load_books()
    
    if not books:
        st.info("Knygų sąrašas tuščias.")
    else:
        for book in books:
            st.markdown("---")
            st.write(f"**ID:** {book.book_id}")
            st.write(f"**Pavadinimas:** {book.book_title}")
            st.write(f"**Autorius:** {book.book_author}")
            st.write(f"**Žanras:** {book.book_genre}")
            st.write(f"**Išleidimo metai:** {book.book_release}")
            st.write(f"**Prieinama:** {book.book_unit} vnt.")
        st.markdown("---")