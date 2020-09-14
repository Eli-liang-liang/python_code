class Solution:
#    def numIdenticalPairs(self, nums: List[int]) -> int:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i<j) and nums[i] == nums[j]:
                    count += 1
        return count

# https://leetcode.com/problems/number-of-good-pairs/
        
nums = [1,2,3,1,1,3]
print(Solution().numIdenticalPairs(nums))
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.



