class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """

    def canWinBash(self, n):
        return self.memoization_search(n, {})

    def memoization_search(self, n, memo):
        if n <= 3:
            return True

        if n in memo:
            return memo[n]

        for i in range(1, 4):
            # n-i 代表第 n-i步是對手走到的:
            if not self.memoization_search(n - i, memo):
                memo[n] = True
                return True

        memo[n] = False
        return False

class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def canWinBash(self, n):
        return n%4 != 0





