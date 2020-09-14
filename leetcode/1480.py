class Solution:
    # def runningSum(self, nums: List[int]) -> List[int]:
    def runningSum(self, nums):
        sums = 0
        for i in range(0, len(nums)):
            sums = sums + nums[i]
            nums[i] = sums  
        return nums


nums = [1,2,3,4]
print(Solution().runningSum(nums))