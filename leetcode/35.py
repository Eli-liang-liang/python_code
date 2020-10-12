class Solution:
    def searchInsert(self, nums, target):
        if target not in nums:
	        nums.append(target)
	        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                x = i
        return x


class Soluion:
    def searchInsert(self, nums, target):
        if target not in nums:
	        nums.append(target)
	        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                x = i
        return x


#class Solution:
#    def searchInsert(self, nums, target):
#        if target not in nums:
#	        nums.append(target)
#	        nums.sort()
#	        x = nums.index(target)
#        else:
#            x = nums.index(target)
#        return x

