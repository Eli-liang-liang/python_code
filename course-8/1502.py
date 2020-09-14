# 1502. 判断能否形成等差数列  https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# arr = list(range(0,100,2))
# arr = [3,5,1]
# ans = true

arr = [1,2,4]
# ans = false

# arr.sort() # 1. 在arr上本身进行修改 2. 不会返回任何东西
# # 直接使用arr
# sorted_arr = sorted(arr) # 1. 不修改arr，将排好序的作为函数返回值，返回到sorted_arr这个变量
# # 需要使用sorted_arr

# for i in sorted(arr):
#     print(i)


ans = True

Arr = sorted(arr)
diff = Arr[1] - Arr[0]
for i in range(len(Arr)-1):
    if (Arr[i+1]- Arr[i]) != diff:
        # print("不是等差数列")
        ans = False
        break
if ans:
    print("是等差数列")
else:
    print("不是等差数列")

    
