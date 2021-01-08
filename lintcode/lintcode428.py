class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n *= -1

        ans = 1
        tmp = x
        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n //= 2
        return ans

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        is_negative = n < 0
        if n == 0:
            return 1
        if n == 1:
            return x
        n = abs(n)
        ans = 0
        result = self.myPow(x, n // 2)
        if n % 2 == 0:
            ans = result * result
        else:
            ans = result * result * x
        if is_negative:
            return 1 / ans

        return ans

class Solution:
    def __init__(self):
        self.visited = {}

    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        if n in self.visited:
            return self.visited[n]

        is_negative = n < 0
        if n == 0:
            return 1
        if n == 1:
            return x
        n = abs(n)
        ans = 0
        if n % 2 == 0:
            ans = self.myPow(x, n // 2) * self.myPow(x, n // 2)
        else:
            ans = self.myPow(x, n // 2 + 1) * self.myPow(x, n // 2)
        if is_negative:
            return 1 / ans

        self.visited[n] = ans
        return ans