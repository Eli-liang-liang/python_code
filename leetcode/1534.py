class Solution:
    def countGoodTriplets(self, arr, a, b,c):
        count = 0
        for i in range(0, len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                       count +=1  
        return count


# class Solution:
#     def countGoodTriplets(self, arr, a, b,c):
#         count = 0
#         for i in range(0, len(arr)):
#             for j in range(i+1,len(arr)):
#                 if abs(arr[i] - arr[j]) <= a:
#                     for k in range(j+1,len(arr)):
#                         if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
#                             count +=1
#         return count