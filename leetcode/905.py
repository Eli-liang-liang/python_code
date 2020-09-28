class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        Returnlist = []
        for i in A:
            if i%2 == 0:
                Returnlist.insert(0, i)
            else:
                Returnlist.append(i)
        return Returnlist