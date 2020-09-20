class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        big = max(A)
        small = min(A)
        if big - small > K:
            big = big - K
            if big - small < K:
                small += big - small
            else:
                small = small + K
            return big - small
        
        if big - small <= K:
            return 0

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A.sort()
        min_n = A[0]
        max_n = A[-1]
        if max_n - min_n <= 2*K:
            return 0
        else:
            return (max_n - min_n - 2*K)

