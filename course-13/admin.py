from user import User

class Admin(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.user_type = "Admin"
        


