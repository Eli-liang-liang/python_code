
# 1
# 3
# 5
# ....

arr = [1,4,2,5,3,6]

ans = 0

# 1，3，5，7，......
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
# 拿到所有大小小于等于len(arr)的奇数 ： l
for l in range(0, len(arr)+1):
    if (l % 2 == 1):
        # 遍历所有长度为l的subarray的开始位置 : j
        for j in range(0,len(arr)-(l-1)):
            # j : 长度为l的subarray的开始位置
            subarray = arr[j:j+l]
            print(subarray)
            s = 0
            for i in subarray:
                s = s+i
            print(s)
            ans += s
            
 


# # 遍历所有长度为3的subarray的开始位置

# for j in range(0,len(arr)-2):
#     # j : 长度为3的subarray的开始位置
#     subarray = arr[j:j+3]
#     print(subarray)
#     s = 0
#     for i in subarray:
#         s = s+i
#     print(s)


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for l in range(1, len(arr) + 1, 2):
            for i in range(len(arr)-(l-1)):
                temp = 0
                for j in range(i, i+l):
                    temp += arr[j]
                s += temp
        return s