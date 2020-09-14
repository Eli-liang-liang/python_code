class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d=dict()
        num=nums.copy()
        # num=nums[:]
        num.sort()
        for i in range(len(num)):
            if num[i] not in d.keys():
                d[num[i]]=i
        for i in range(len(nums)):
            nums[i]=d[nums[i]]
        return nums