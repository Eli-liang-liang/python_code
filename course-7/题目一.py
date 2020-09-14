# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

nums = [8, 1, 2, 2, 3]

# ans = [4,0,1,1,3]
list1 = []
for a in nums:
    # 得到一个count，这个count包含了小于8的数字的个数
    count = 0
    for i in nums:
        if i < a:
            count += 1
    list1.append(count)

print(list1)
    