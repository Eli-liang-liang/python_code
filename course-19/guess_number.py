# 1. 计算机出一个1到100之间的随机数（可以通过python的内置函数完成）
# 2. 玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），不断循环，直到玩家猜中了数字
#       a. 如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续

import random
number = random.randint(1,100)
guess = 0
time = 0
while (guess != number):
    valid = False
    while(not valid):
        A = input("guess number")
        try:
            guess = int(A)
        except ValueError:
            valid = False
            print("Your input is not digit, please input again!")
            continue
        valid = True

    if guess == number:
        print("right")
    else:
        if guess > number:
            print("too big")
        else:
            print("too small")
    time += 1
print("game over,you try:", time, "times")