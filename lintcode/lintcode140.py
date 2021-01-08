class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b

        ans = 1

        while n != 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = (a % b) * (a % b)
            n //= 2
        return ans


class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
        if n == 1:
            return a % b

        product = self.fastPower(a, b, n // 2)
        product = (product * product) % b

        if n % 2 == 1:
            product = (product * a) % b

        return product
