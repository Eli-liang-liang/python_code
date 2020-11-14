# def gcd(x, y):
#     for i in range(min(x,y),0,-1):
#         if x % i == 0 and y % i == 0:
#             return i


# def lcm(x, y):
#     i = gcd(x,y)
#     a = x // i
#     b = y // i
#     return(a*b*i)
    
# print(lcm(4,6))

# def is_prime(num):
#     """判断一个数是不是素数"""
#     a = 0
#     b = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             if i == 1 or i == num:
#                 continue
#             a  = i
#             b = num // i
#     if num ==1:
#         return False 
#     else:
#         if a == 0 and b==0:
#             return True 
#         else:
#             return False


# print(is_prime(15))


class Solution:
    def countPrimes(self, n):
        # 2-n
        if (n <= 2):
            return 0
        # 0 .... n (n+1)  isPrime[i] = 1
        isPrimes = [1 for i in range(n)] # isPrimes[i] == 1 , i is Prime 不管[0-1]
        for i in range(2, n/2):
            if isPrimes[i] == 1:
                times = 2
                while(i*times < n):
                    isPrimes[i*times] = 0
                    times += 1
        count = 0
        for i in range(2, n):
            if isPrimes[i] == 1:
                count += 1
        return count



class Solution:
    def countPrimes(self, n):
        # 2-n
        if (n == 0 and n == 1):
            return 0
        if n == 2:
            return 1
        # 0 .... n (n+1)  isPrime[i] = 1
        isPrimes = [1 for i in range(n+1)] # isPrimes[i] == 1 , i is Prime 不管[0-1]
        for i in range(2, n+1):
            if isPrimes[i] == 1:
                times = 2
                while(i*times <= n):
                    isPrimes[i*times] = 0
                    times += 1
        count = 0
        for i in range(2, n+1):
            if isPrimes[i] == 1:
                count += 1
        return count



class Solution:
    def is_prime(self,num):
        a = 0
        b = 0
        for i in range(1,num+1):
            if num % i == 0:
                if i == 1 or i == num:
                    continue
                a  = i
                b = num // i
        if num == 1:
            return False
        if a == 0 and b==0:
            return True 
        else:
            return False
        
    def countPrimes(self, n):
        a = 0
        for i in range(2,n+1):
            if self.is_prime(i) == True and i < n:
                a+=1

            
        print(a)

a = Solution()
a.countPrimes(0)

