# 1342. 将数字变成 0 的操作次数  https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
num =  123
count = 0
while num > 0:
    if num%2 == 0:
        num = num/2
    else:
        num -= 1
    count += 1

print(count)




# ans = 6