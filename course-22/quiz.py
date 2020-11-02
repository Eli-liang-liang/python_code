# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

# 说明：

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。

# 示例：

# 输入：
# nums1 = [1,2,3], m = 3
# nums2 = [2,5,6], n = 3

# # 输出：[1,2,2,3,5,6]


def mergeSortedArray(nums1, nums2):
    s = []
    i = 0
    j = 0
    while(i <= (len(nums1)-1) and j <= (len(nums2)-1)):
        if nums1[i] < nums2[j]:
            s.append(nums1[i])
            i += 1
        else:
            s.append(nums2[j])
            j += 1
        
    while(i <= (len(nums1)-1)):
        s.append(nums1[i])
        i += 1

    while(j <= (len(nums2)-1)):
        s.append(nums2[j])
        j += 1
    return s

print(mergeSortedArray([1,2,3],[2,5,6]))  





class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_list=list(num1)
        num2_list=list(num2)
        sum1=sum2=0
        for num in num1_list:
            sum1=sum1*10+int(num)
        for num in num2_list:
            sum2=sum2*10+int(num)
        return str(sum1+sum2)

# class ParkingSystem(object):

#     def __init__(self, big, medium, small):
#         self.big = big
#         self.medium = medium
#         self.small = small
        

#     def addCar(self, carType):
#         if carType == 1 and self.big > 0:
#             self.big -=1
#             return True
#         elif carType == 2 and self.medium > 0:
#             self.medium -=1
#             return True
#         elif carType == 3 and self.small > 0:
#             self.small -=1
#             return True
#         return False
        

# class Solution:
#     def threeConsecutiveOdds(self, arr: List[int]) -> bool:
#         count = 0
#         for i in range(len(arr)):
#             if arr[i] % 2 != 0:
#                 count += 1 
#                 if count == 3:
#                     return True
#             else:
#                 count = 0
#         return False

