class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for num in arr:
            if num not in s:
                if num % 2 ==  0:
                    s.add(num//2)
                s.add(num*2)
            else:
                return True
        return False
        