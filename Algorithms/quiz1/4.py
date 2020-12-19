class Solution:
    def mysort(self,nums):
        for i in range(0,len(nums)):
            index_chose = i
            for a in range(i, len(nums)):
                if nums[a] < nums[index_chose]:
                    index_chose = a
            nums[i], nums[index_chose] = nums[index_chose], nums[i]
        return nums


    def containsDuplicate(self,nums):
    # add some code
        nums = self.mysort(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    
    
# test
print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))