def find_target(nums, target):
    for i in nums:
        if i == target:
            return True
    return False



nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


print(find_target(nums, 0))
print(find_target(nums, 3))
print(find_target(nums,11))
print(find_target(nums,16))
print(find_target(nums,17))