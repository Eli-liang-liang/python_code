A = open("guest.txt", "w")
C = open("allowlist.txt", "r")
#B = A.read()
D = C.read()

while True:
    E = input("name:")
    if E in D:
        A.write(E+"\n")
        A.flush()
        # A.write("\n")
        print("welcome")

    elif E =="quit":
        break
    else:
        print("你没有权限")

A.close()
C.close()

# pwd
# /Users/qifeng/python_code
# /Users/qifeng/python_code/python_code/course-16

# cd python_code/course-16