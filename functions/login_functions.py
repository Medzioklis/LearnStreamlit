from classes.user import User
from . import data_functions as df

def login(username, password):
    users = df.load_users()
    for user in users:
        if user.user_id == username and user.user_password == password:
            return user
    return None

def create_initial_fakeadmin():
    users = df.load_users()
    if not users:
        admin = User(user_id="admin", user_name="Administratorius", user_password="admin", user_role="bibliotekininkas")
        df.save_users([admin])
        print("Programos startui sukurtas fake admin vartotojas")