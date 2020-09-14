# https://leetcode.com/problems/shuffle-the-array/

# nums = [2,5,1,3,4,7]
# n = 3
# i,j=0,n
# c=[]
# while i<n:
#     c.append(nums[i])
#     c.append(nums[j])
#     i+=1
#     j+=1



# def shuffle(nums, n):

# # int: integer 整数
# # List : 列表
# # List[int]: 存放整数的列表
# def shuffle(nums, n) -> List[int]:
# def shuffle(nums: List[int], n: int) -> List[int]:
def shuffle(nums, n):
    c = []
    i,j=0,n
    while i<n:
        c.append(nums[i])
        c.append(nums[j])
        i+=1
        j+=1
    return c


print(shuffle([2,5,1,3,4,7], 3))