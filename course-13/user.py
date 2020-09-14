class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.id = 0

    def set_user_id(self, id):
        self.id = id

    def get_user_id(self):
        return self.id

    def print_user_info(self):
        print("name:" + self.name)
        print("age:"+ self.age)
        print("gender:" + self.gender)


manA = User("👴", "18", "man") 
manA.print_user_info()




