class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = 0
        self.user_type = "User"

    def set_user_id(self, id):
        self.id = id

    def get_user_id(self):
        return self.id
    
    def get_user_type(self):
        print(self.user_type)
        return self.user_type

    def print_user_info(self):
        print("name:" + self.name)
        print("age:"+ self.age)
        print("gender:" + self.gender)

    def set_password(self, password):
        self.password = password
    
    def login(self, user_input_password):
        if user_input_password == self.password:
            print("login success")
        else:
            print("login failed")
            
# Admin继承自User
# Admin类需要设置user_type，Admin类的用户类型为“Admin”



