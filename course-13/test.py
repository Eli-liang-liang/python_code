
from user import User
from admin import Admin

manA = User("👴", "18", "man") 
manA.print_user_info()

manA.set_password("123456pass")
manA.login("123456pass")



adminA = Admin("👮‍♀️", "19", "man")
adminA.get_user_type()

