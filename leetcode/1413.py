class Solution:
    def minStartValue(self, nums):
        startValue = 1

        while startValue:
            if judgeStartValue(nums, startValue):
                return startValue
            startValue += 1

def judgeStartValue(nums, startValue):
    for i in nums:
        startValue += i
        if startValue < 1:
            return False
    return True
    

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        def isOk(startValue):
            s = startValue
            for n in nums:
                s += n
                if s < 1:
                    return False
            return True
        for i in range(1, 3000):
            if isOk(i):
                return i
        return 0


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minValue = 1
        s = 0
        for n in nums:
            s += n
            minValue = min(minValue, s)
        if minValue >= 1:
            return 1
        else:
            return 1-minValue