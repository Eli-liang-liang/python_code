while 1:
    try:
        a = float(input("a : "))
        b = float(input("b : "))
        print("a/b:", a/b)
    except ValueError:
        print("You should use number as a and b")
    except ZeroDivisionError:
        print("You can't divide by zero!")


# while 1:
#     try:
#         a = float(input("a : "))
#     except ValueError:
#         print("You can not use string as a")
#         continue

#     b = float(input("b : "))

#     try:
#         print("a/b:", a/b)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")


# print(5/0)