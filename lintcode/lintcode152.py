"""
redudant!! nums is unnecessary
"""
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        nums = [i + 1 for i in range(n)]
        combinations = []
        self.dfs(nums, 0, [], combinations, k)
        return combinations

    def dfs(self, nums, index, comb, combinations, k):
        if k == 0:
            combinations.append(comb[:])
            return
        if index >= len(nums):
            return

        for i in range(index, len(nums)):
            comb.append(nums[i])
            self.dfs(nums, i + 1, comb, combinations, k - 1)
            comb.pop()

"""
more simple
"""

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        combinations = []
        self.dfs(n, 1, [], combinations, k)
        return combinations

    def dfs(self, n, start, comb, combinations, k):
        if k == 0:
            combinations.append(comb[:])
            return

        for i in range(start, n + 1):
            comb.append(i)
            self.dfs(n, i + 1, comb, combinations, k - 1)
            comb.pop()
