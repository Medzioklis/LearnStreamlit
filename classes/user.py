class User():
    def __init__(self, user_id, user_name, user_password, user_role):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role 
    
    def __str__(self):
        return (f"|| ID: {self.user_id} || Vardas ir pavardė: {self.user_name} || Rolė: {self.user_role} ||")


            
    
    
    
