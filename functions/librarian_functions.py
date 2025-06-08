import streamlit as st
from classes.user import User
from . import data_functions as df

user_file = "data/users.pickle"

def create_user():
    st.subheader("Sukurti vartotoją")
    users = df.load_users()
    
    with st.form("create_user_form", clear_on_submit=True):
        user_name = st.text_input("Įveskite vartotojo vardą ir pavardę:")
        user_password = st.text_input("Įveskite slaptažodį:", type="password")
        user_role = st.radio("Pasirinkite rolę:", ("skaitytojas", "bibliotekininkas"))
        
        submitted = st.form_submit_button("Sukurti")
        
        if submitted:
            if user_name and user_password:
                user_id = df.get_id() # Ensure get_id is appropriate for Streamlit (e.g., incremental)
                user = User(user_id, user_name, user_password, user_role)
                users.append(user)
                df.save_users(users)
                st.success(f"Vartotojas: **{user.user_name}** sukurtas. Kortelės numeris: **{user.user_id}**, slaptažodis: **{user.user_password}**, rolė: **{user.user_role}**")
            else:
                st.error("Prašome užpildyti visus laukus.")

def delete_user():
    st.subheader("Ištrinti vartotoją")
    users = df.load_users()
    
    user_id_to_delete = st.text_input("Įveskite vartotojo kortelės numerį, kurį norite ištrinti:")
    
    if st.button("Ištrinti vartotoją"):
        original_len = len(users)
        users = [user for user in users if user.user_id != user_id_to_delete]
        if len(users) < original_len:
            df.save_users(users)
            st.success(f"Vartotojas su ID: **{user_id_to_delete}** ištrintas.")
        else:
            st.error(f"Vartotojas su ID **{user_id_to_delete}** nerastas.")

def update_user():
    st.subheader("Atnaujinti vartotoją")
    users = df.load_users()
    
    user_id_to_update = st.text_input("Įveskite vartotojo ID, kurį norite atnaujinti:")
    
    if user_id_to_update:
        found_user = None
        for user in users:
            if user.user_id == user_id_to_update:
                found_user = user
                break
        
        if found_user:
            st.write(f"Atnaujinamas vartotojas: **{found_user.user_name}** (ID: {found_user.user_id})")
            
            with st.form("update_user_form"):
                new_user_name = st.text_input("Naujas vartotojo vardas ir pavardė (palikite tuščią, jei nekeičiate):", value=found_user.user_name)
                new_user_password = st.text_input("Naujas slaptažodis (palikite tuščią, jei nekeičiate):", type="password")
                
                current_role_index = 0
                if found_user.user_role == "bibliotekininkas":
                    current_role_index = 1
                new_user_role = st.radio(f"Nauja rolė (dabar: {found_user.user_role}):", ("skaitytojas", "bibliotekininkas"), index=current_role_index)
                
                submitted = st.form_submit_button("Atnaujinti")
                
                if submitted:
                    if new_user_name:
                        found_user.user_name = new_user_name
                    if new_user_password:
                        found_user.user_password = new_user_password
                    if new_user_role: # Streamlit radio will always return a value
                        found_user.user_role = new_user_role
                    
                    df.save_users(users)
                    st.success(f"Vartotojas: **{found_user.user_name}** atnaujintas. Kortelės numeris: **{found_user.user_id}**, rolė: **{found_user.user_role}**")
        else:
            st.error("Vartotojas nerastas.")


def list_users():
    st.subheader("Vartotojų sąrašas")
    users = df.load_users()
    
    if not users:
        st.info("Vartotojų sąraše nėra.")
    else:
        for user in users:
            st.markdown(f"---")
            st.write(f"**ID:** {user.user_id}")
            st.write(f"**Vardas:** {user.user_name}")
            st.write(f"**Rolė:** {user.user_role}")
        st.markdown("---")