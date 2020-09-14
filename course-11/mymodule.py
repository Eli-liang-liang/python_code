class Solution:
    def toLowerCase(self, str):
        letter = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
             'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
             'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
             'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
             'U': 'u', 'V': 'v', 'X': 'x', 'W': 'w', 'Y': 'y',
             'Z': 'z'}
        for i in str:
            if i in letter:
                str = str.replace(i, letter[i])
        return str

def test():
    print("test")

# Solution().toLowerCase("abc")

# # ASCII table
# class Solution:
#     def toLowerCase(self, str: str) -> str:
#         str_list = list(str)
#         for i in range(len(str_list)):
#             c = str_list[i]
#             if ord('A') <= ord(c) and ord(c) <= ord('Z'):
#                 # c是大写字符
#                 str_list[i] = chr(ord(c)+(ord('a')-ord('A')))
#         return "".join(str_list)