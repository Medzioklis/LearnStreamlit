import streamlit as st
from datetime import datetime, timedelta
from classes.basket import Basket
from . import data_functions as df
from . import book_function as bf


def book_basket_streamlit(user):
    st.subheader("Paimti knygą")
    books = df.load_books()
    baskets = df.load_baskets()

  
    overdue_found = False
    for book_in_basket in baskets:
        if book_in_basket.user_id == user.user_id:
            days = (datetime.now() - book_in_basket.basket_date).days
            if days > 14:
                st.warning(f"Turite perlaikytą knygą **{book_in_basket.book_title}**, todėl negalite imti naujų knygų.")
                overdue_found = True
                break
    
    if overdue_found:
        return

    st.write("Visos prieinamos knygos:")
    bf.list_books() 

    with st.form("take_book_form", clear_on_submit=True):
        book_title = st.text_input("Įveskite knygos pavadinimą, kurią norite paimti:")
        submitted = st.form_submit_button("Paimti knygą")

        if submitted:
            found_book = None
            for book in books:
                if book.book_title == book_title:
                    found_book = book
                    break
            
            if found_book:
                if found_book.book_unit <= 0:
                    st.error("Knygos šiuo metu nėra sandėlyje.")
                    return
                
                if any(b.book_title == book_title and b.user_id == user.user_id for b in baskets):
                    st.warning("Jūs jau pasiskolinote šią knygą.")
                    return
                
                found_book.book_unit -= 1
                new_basket = Basket(user.user_id, user.user_name, found_book.book_id, found_book.book_title)
                baskets.append(new_basket)
                df.save_books(books)
                df.save_baskets(baskets)
                
                return_date = datetime.now() + timedelta(days=14)
                st.success(f"Knyga **{found_book.book_title}** paimta. Privalote grąžinti iki: **{return_date.strftime('%Y-%m-%d')}**")
            else:
                st.error("Knyga nerasta.")
    

def return_book(user):
    st.subheader("Grąžinti knygą")
    baskets = df.load_baskets()
    books = df.load_books()
    user_baskets = [book for book in baskets if book.user_id == user.user_id]

    if not user_baskets:
        st.info("Neturite pasiskolintų knygų.")
        return

    st.write("Jūsų pasiskolintos knygos:")
    for book in user_baskets:
        st.markdown(f"**Pavadinimas:** {book.book_title}, **Paimta:** {book.basket_date.strftime('%Y-%m-%d')}")
    
    with st.form("return_book_form", clear_on_submit=True):
        book_title_to_return = st.text_input("Įveskite knygos pavadinimą, kurią norite grąžinti:")
        submitted = st.form_submit_button("Grąžinti knygą")

        if submitted:
            initial_basket_len = len(baskets)
            baskets = [book for book in baskets if not (book.user_id == user.user_id and book.book_title == book_title_to_return)]
            
            if len(baskets) < initial_basket_len: # If a book was actually removed from the basket
                for book in books:
                    if book.book_title == book_title_to_return:
                        book.book_unit += 1
                        break
                df.save_books(books)
                df.save_baskets(baskets)
                st.success(f"Knyga **{book_title_to_return}** grąžinta.")
            else:
                st.error("Nepavyko grąžinti knygos. Patikrinkite pavadinimą.")



def view_my_books(user):
    st.subheader("Mano pasiskolintos knygos")
    baskets = df.load_baskets()
    user_baskets = [book for book in baskets if book.user_id == user.user_id]
    
    if not user_baskets:
        st.info("Neturite pasiskolintų knygų.")
    else:
        for book in user_baskets:
            st.markdown("---")
            st.write(f"**Pavadinimas:** {book.book_title}")
            st.write(f"**Paimta:** {book.basket_date.strftime('%Y-%m-%d')}")
            
            days = (datetime.now() - book.basket_date).days
            if days > 14:
                st.warning(f"**PERLAIKYTA!** Knyga perlaikyta **{days - 14}** dienų.")
            else:
                st.info(f"Liko dienų grąžinti: **{14 - days}**")
        st.markdown("---")
