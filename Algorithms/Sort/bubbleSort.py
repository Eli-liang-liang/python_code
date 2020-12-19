# def mysort(nums):
#     # add some code
#     # 确定第二层循环的范围
#     for i in range(len(nums)-1, 0, -1):
#         # 此次循环，目的是将nums[i]填对，也就是在范围[0,i]内冒泡
#         for j in range(0, i):
#             # [0, i-1]
#             if nums[j] > nums[j+1]:
#                 # swap nums[j] and nums[j+1]
#                 temp = nums[j+1]
#                 nums[j+1] = nums[j]
#                 nums[j] = temp
#     return nums


# def bubbleSort(arr):
#     for i in range(1, len(arr)):
#         for j in range(0, len(arr)-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
    
# nums = [ 3,4,7,4,1,8,0,5 ]
# print(mysort(nums)) # print [0,1,3,4,4,5,7,8]

