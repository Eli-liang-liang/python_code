name = "Amy"

# 写入guest.txt
# A = open("guest.txt", "r") # 默认
# cd python_code/course-16 # 改变终端所处的当前目录
A = open("guest.txt", "w")
# A = open("guest.txt", "a")
A.write(name)
A.close()