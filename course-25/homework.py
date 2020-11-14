
# def f(n,x):
#     a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
#     b=[]
#     while True:
#         s=n//x  
#         y=n%x  
#         b=b+[y]
#         if s==0:
#             break
#         n=s
#     b.reverse()
#     for i in b:
#         print(a[i],end='')
# f(185,2)
# print()
# f(185,8)
# print()
# f(185,16)
# print()


def b(num,n):
    baseStr = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
               "a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19}
    new_num = 0
    NB = len(num) - 1
    for i in num:         
        new_num = new_num  + baseStr[i]*pow(n,NB)
        NB = NB -1 
    return new_num

print(b("10111001", 2))
print(b("271", 8))
print(b("b9", 16))
