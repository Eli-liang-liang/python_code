class Solution:
    def repeatedNTimes(self, A):
        N = len(A)/2
        for i in range(len(A)):
            if A.count(A[i]) == N:
                return A[i]

# 时间复杂度

# class Solution:
#     def repeatedNTimes(self, A: List[int]) -> int:
#         N = len(A)/2
#         m = {}
#         for i in range(len(A)):
#             m[A[i]] = 0
#             # { 1 : 0, 2: 0, 3 : 0}
#         for i in range(len(A)):
#             m[A[i]] += 1
#             if m[A[i]] == N:
#                 return A[i]
#         return 0