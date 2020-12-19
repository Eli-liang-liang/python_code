# def find_target(nums, target):
#     # add your code
#     low, high = 0, len(nums) - 1
#     while low <= high:
#         mid = (high + low) // 2
#         if nums[mid] < target:
#             low = mid + 1
#         elif nums[mid] > target:
#             high = mid -1
#         else:
#             return True
#     return False

# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


# print(find_target(nums, 0))
# print(find_target(nums, 3))
# print(find_target(nums,11))
# print(find_target(nums,16))
# print(find_target(nums,17))