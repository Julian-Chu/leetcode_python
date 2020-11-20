class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    cache = {}

    def fibonacci(self, n):
        if n <= 2:
            return n - 1

        if n in self.cache:
            return self.cache[n]

        value = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        self.cache[n] = value
        return value


class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    cache = {}

    def fibonacci(self, n):
        a, b = 0, 1

        for _ in range(n - 1):
            a, b = b, a + b
        return a
