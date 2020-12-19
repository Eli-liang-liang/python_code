# def Selectionsort(nums):
#     for a in range(0, len(nums)):
#         index_chosen = a
#         for i in range(a,len(nums)):
#             if nums[i] < nums[index_chosen]:
#                 index_chosen = i
#         nums[a],nums[index_chosen] = nums[index_chosen],nums[a]
#     return nums
# nums = [ 3,4,7,4,1,8,0,5 ]

# print(Selectionsort(nums))

# def count_bits(n):
#     res = 0
#     while n != 0:
#         res += n % 2
#         n = n //2
#     return res

# print(count_bits(11))
# print(bin(11))
class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    # 用于在print中直接打印Point
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    # 用于在print中直接打印Point
    def __repr__(self):
        return "({},{})".format(self.x, self.y)

def smallerThan(p1, p2):
    if (p1.x > p2.x):
        return True
    elif (p1.x == p2.x and p1.y > p2.y):
        return True
    return False


def mysort(arrayOfPoints):
    lenOfArray = len(arrayOfPoints)
    for i in range(lenOfArray):
        # find the min of (i -  lenOfArray-1 )
        minIndex = i
        for j in range(i, lenOfArray):
            if smallerThan(arrayOfPoints[j], arrayOfPoints[minIndex]):
                minIndex = j
        # get minIndex, than swap i, minIndex
        temp = arrayOfPoints[minIndex]
        arrayOfPoints[minIndex] = arrayOfPoints[i]
        arrayOfPoints[i] = temp
    return arrayOfPoints
    
    
points = [ Point(1,2), Point(1,4), Point(4,5), Point(5,6), Point(4,3) ]
print(mysort(points))