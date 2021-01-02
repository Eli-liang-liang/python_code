import time 

# def sumO(n):
#     start = time.time()

#     theSum = 0
#     for i in range(1, n+1):
#         theSum += i
    
#     end =  time.time()

#     return theSum, end-start

# print(sumO(100000))

# print(sumO(100000))

# print(sumO(1000000))

# print(sumO(1000000))

# print(sumO(1000000))


# def sum1(n):
#     start = time.time()

#     theSum = (n*(n+1))/2
    
#     end =  time.time()

#     return theSum, end-start

# print(sum1(100000))

# print(sum1(100000))

# print(sum1(1000000))

# print(sum1(1000000))

# print(sum1(1000000))

# import numpy as np
# import matplotlib.pyplot as plt

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C,S = np.cos(X), np.sin(X)

# plt.plot(X,C)
# plt.plot(X,S)

# plt.show()


def POP0(n):
    start = time.time()

    n.pop(0)
    end =  time.time()

    return end-start

def POP_(n):
    start = time.time()

    n.pop()
    end =  time.time()

    return end-start


a = []
for i in range(0,200000):
    a.append(i)

b = []
for yue in range(0,400000):
    b.append(yue)

c = []
for Q in range(0,600000):
    c.append(Q)


print(POP0(a))

print(POP_(a))


print(POP0(b))

print(POP_(b))

print(POP_(c))

print(POP0(c))


# def listsearch(n,val):
#     start = time.time()
#     for i in n:
#         if i == val:
#             return True
#             break
#         else:
#             continue
#     end =  time.time()
#     return end-start


# def dicsearch(n,val):
#     start = time.time()
#     for i in n.values():
#         if i == val:
#             return True
#             break
#         else:
#             continue
#     end =  time.time()
#     return end-start

# dic = {'a':"b", 'b':"a"}

# print(dicsearch(dic,"c"))
import numpy as np
import matplotlib.pyplot as plt
x = [200000, 400000, 600000]

y_pop0 = [POP0(a),POP0(b),POP0(c)]
y_pop_ = [POP_(a),POP_(b),POP_(c)]

plt.plot(x,y_pop0)
plt.plot(x,y_pop_)
plt.show()
