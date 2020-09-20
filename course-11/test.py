import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

######################################################################################3

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

###########################################


from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#############################################################################

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

###################################################

from pizza import *
from pizza import make_pizza, test

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
test()


# pizza.test()


# true
# from mymodule import Solution
# str1 = "Hello"
# print(Solution().toLowerCase(str1))

# from mymodule import test

# from Solution import toLowerCase # 模块名：mymodule
# from mymodule import toLowerCase # 该名字不可见

# import calculator as c1
# import calculator2 as c2

# N1 = 2
# N2 = 3
# print(c1.Sum(N1,N2))
# print(c2.Sum(N1,N2))

# from calculator2 import Sum as b
# from calculator import Sum
# N1 = 2
# N2 = 3
# print(Sum(N1,N2))
# print(b(N1,N2))
