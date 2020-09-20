
class Solution:
    def singleNumber(self, nums):
        s = []
        for i in nums:
            if i not in s:
                s.append(i)
            elif i in s:
                s.remove(i)
        return s[0]
 
