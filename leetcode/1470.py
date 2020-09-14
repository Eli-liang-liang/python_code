class Solution:
#    def shuffle(self, nums: List[int], n: int) -> List[int]:
    def shuffle(self, nums, n):
        i,j=0,n
        c=[]
        while i<n:
            c.append(nums[i])
            c.append(nums[j])
            i+=1
            j+=1
        return c

nums = [2,5,1,3,4,7]
n = 3
print(Solution().shuffle(nums,n))