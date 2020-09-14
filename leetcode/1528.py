# class Solution:
#     def restoreString(self, s, indices):
#         a = []
#         new_s = list(s)
#         for i in indices:
#             a.append(new_s[i])
#         A = "".join(a)
#         return A

# s ="aiohn"
# indices= [3,1,4,2,0]
# print(Solution().restoreString(s, indices))


# class Solution:
#     def restoreString(self, s, indices):
#         # new_list = ['' for _ in range(len(indices))]
#         ori_list = list(s)
#         new_list = []
#         for i in range(len(indices)):
#             new_list.append('')
#         # new_list 里放 len(indices) 个 ''
#         # new_list = ['','','','','','','','']
#         # new_list = ['l','e','e','t','c','o','d','e']
#         for i in range(len(indices)):
#             # i = 0
#             # indices[i] = 4
#             # ori_list[i] = 'c'
#             # 将 ori_list[i] 放到  new_list[indices[i]]
#             new_list[indices[i]] = ori_list[i]
#         return "".join(new_list)




class Solution:
    def restoreString(self, s, indices):
        new_s  =  [""] * len(s)
        for i in range(len(s)):
            new_s[indices[i]] = s[i]
        return "".join(new_s) 

s = "aiohn"
indices = [3,1,4,2,0]
print(Solution().restoreString(s, indices))