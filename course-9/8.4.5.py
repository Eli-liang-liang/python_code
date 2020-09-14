nums = [1,2,3]

# 浅复制
nums2 = nums
# 深复制
nums3 = nums[:]

# # print(nums[1:2])

nums2[0] = 4
nums3[0] = 4

print(nums)
print(nums2)
print(nums3)



def modify_nums(nums2):
    nums2[0] = 4

nums = [1,2,3]
# # modify_nums(nums)
modify_nums(nums[:])

# print(nums)