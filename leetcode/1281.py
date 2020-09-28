class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product,sum1 = 1,0
        while n:
            digit = (n%10)
            product *= digit
            sum1 = sum1 + digit
            n //= 10

        return product - sum1