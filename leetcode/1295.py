# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         count = 0
#         for i in nums:
#             if 10 <= i <= 99 or 1000 <= i <= 9999 or i == 100000:
#                 count += 1
#         return count

class Solution:
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            if len(str(i))%2 == 0:
                count += 1
        return count
                
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         def countN(n):
#             count = 0
#             while(n):
#                 count += 1
#                 n = n//10
#             return count
#         count = 0
#         for n in nums:
#             if countN(n) % 2 == 0:
#                 count+=1
#         return count