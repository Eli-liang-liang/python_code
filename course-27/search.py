# def find_target(nums, target):
#     for i in nums:
#         if i == target:
#             return True
#     return False



# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


# print(find_target(nums, 0))
# print(find_target(nums, 3))
# print(find_target(nums,11))
# print(find_target(nums,16))
# # print(find_target(nums,17))
# class Solution:
#     def A(self,nums):
#         B = {}
#         for i in nums:
#             if B.get(i) == None:
#                 B[i] = 1
#             else:
#                 B[i] += 1
#         self.B = B
            

#     def Smallerthan(self,a,b):
#         if self.B[a] < self.B[b]:
#             return True
#         elif self.B[a] == self.B[b] and a > b:
#             return True
#         else:
#             return False
    
#     def frequencySort(self, nums):
#         self.A(nums)
#         for a in range(0,len(nums)):
#             index_chose = a
#             for i in range(a, len(nums)):
#                 if self.Smallerthan(nums[i],nums[index_chose]):
#                     index_chose = i
#             nums[a],nums[index_chose] = nums[index_chose], nums[a] 
#         return nums


# BBBB = Solution()
# print(BBBB.frequencySort([1,1,2,2,2,3]))

            


# def move(n,f,buffer,to):
#     count = 0
#     if n==1:
#         print('from',f,'to',to)
#         return 1
#     else:
#         count += move(n-1,f,to,buffer)
#         count += move(1,f,buffer,to)
#         count += move(n-1,buffer,f,to)
#     return (count)

# print(move(3,"A","B","C"))

# def reverse(num):
#     ret=0
#     while num:
#         last=num%10
#         ret=ret*10+last
#         num//=10
#     return ret


# def B(s):
#     s = str(s)
#     if len(s) <= 1:
#         return s
#     return int(s[-1] + B(s[:-1]))

# print(B(34))

# def merge(arr1, arr2):
#     i1 = 0
#     i2 = 0
#     arr1_len = len(arr1)
#     arr2_len = len(arr2)
#     arr = []
#     while(i1 < arr1_len and i2 < arr2_len):
#         if arr1[i1] < arr2[i2]:
#             arr.append(arr1[i1])
#             i1 += 1
#         else:
#             arr.append(arr2[i2])
#             i2 += 1
#     while(i1 < arr1_len):
#         arr.append(arr1[i1])
#         i1 += 1
#     while(i2 < arr2_len):
#         arr.append(arr2[i2])
#         i2 += 1
#     return arr
# def mergeSort(arr):
#     if(len(arr)<2):
#         return arr
#     middle = len(arr)//2
#     left, right = arr[0:middle], arr[middle:]
#     return merge(mergeSort(left), mergeSort(right))


# b = [8,4,5,7,1,3,6,2]
# print(mergeSort(b))

# def bubbleSort(alist):
#     count = 0
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i]>alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#             count += 1
#     print(count)
#     return alist

# def Selection(A):
#     count = 0
#     for i in range(len(A)): 
#         min_idx = i 
#         for j in range(i+1, len(A)): 
#             if A[min_idx] > A[j]: 
#                 min_idx = j
#             count += 1 
#         A[i], A[min_idx] = A[min_idx], A[i]
#     print(count)


def merge(arr1, arr2):
    i1 = 0
    i2 = 0
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    arr = []
    while(i1 < arr1_len and i2 < arr2_len):
        if arr1[i1] < arr2[i2]:
            arr.append(arr1[i1])
            i1 += 1
        else:
            arr.append(arr2[i2])
            i2 += 1
    while(i1 < arr1_len):
        arr.append(arr1[i1])
        i1 += 1
    while(i2 < arr2_len):
        arr.append(arr2[i2])
        i2 += 1
    return arr
def mergeSort(arr):
    if(len(arr)<2):
        return arr
    middle = len(arr)//2
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

c = [1,2,3,4,5]
mergeSort(c)