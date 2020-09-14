

class Solution:
    def canMakeArithmeticProgression(self,arr):
        ans = True
        Arr = sorted(arr)
        diff = Arr[1] - Arr[0]
        for i in range(len(Arr)-1):
            if (Arr[i+1]- Arr[i]) != diff:
                # print("不是等差数列")
                ans = False
                break
        if ans:
            print("是等差数列")
        else:
            print("不是等差数列")
        return ans

arr = [1, 2, 4]
print(Solution().canMakeArithmeticProgression(arr))
    