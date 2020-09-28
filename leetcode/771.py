class Solution:
#    def numJewelsInStones(self, J: str, S: str) -> int:
    def numJewelsInStones(self, j,s):
        count = 0
        for a in s:
            if a in j:
                print(a, "是一个宝石")
                count += 1
            else:
                continue
        return count


j = "aA"
s = "aAAbbbb"
print("宝石一共有：", Solution().numJewelsInStones(j,s), "个")


