# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

# 说明：

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。

# 示例：

# 输入：
# nums1 = [1,2,3], m = 3
# nums2 = [2,5,6], n = 3

# 输出：[1,2,2,3,5,6]

class Solution:
    def A(nums1, nums2, m, n):
        i = 0
        j = 0
        while(i <= m-1 and j <= n-1 ):
            if nums2[j] <= nums1[i] :
                nums1.insert(i , nums2[j])
                m += 1
                nums1.pop()
                j += 1
            i += 1
        
        if j < n :
            
            for x in range(n-j):
                nums1[-(x+1)] = nums2[-(x+1)]

nums1 = [1,2,3]
nums2 = [2,5,6]
print(A(nums1, nums2,3,3))