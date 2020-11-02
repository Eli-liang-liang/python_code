# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# nums = [8, 1, 2, 2, 3]

# # ans = [4,0,1,1,3]
# list1 = []
# for a in nums:
#     # 得到一个count，这个count包含了小于8的数字的个数
#     count = 0
#     for i in nums:
#         if i < a:
#             count += 1
#     list1.append(count)

# print(list1)

def can1(arr):
    b = True 
    arr.sort()
    s = arr[1]-arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != s:
            b = False
            break
    return b    
print(can1([1,2,4,5]))  


