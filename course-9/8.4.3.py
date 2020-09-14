m = 3
def double_test(n):
    global m
    m = m*2
    return m

def double(n):
    n = n*2
    return n 

print(double(3))
print(double(3))
print(double(3))

print(double_test(4)) 
print(double_test(4))
print(double_test(4))
