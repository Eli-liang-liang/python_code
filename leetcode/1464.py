# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         A = (nums[len(nums)-1]-1)*(nums[len(nums)-2]-1)
#         return A

class Solution:
    def maxProduct(self, nums):
        max_result = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                # (nums[i],nums[j])
                cur_result = (nums[i]-1)*(nums[j]-1)
                if cur_result > max_result:
                    max_result = cur_result
        return max_result
        

# 时间复杂度：衡量程序的运行时间


# [5,2,6,2]
# (5-1)*(2-1)
# (5-1)*(6-1)
# ...