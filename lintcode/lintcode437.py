"""
@param pages: an array of integers
@param k: An integer
@return: an integer
"""


def copyBooks(self, pages, k):
    # write your code here
    if not pages:
        return 0

    if k > len(pages):
        k = len(pages)
    start, end = 0, sum(pages)
    while start + 1 < end:
        mid = (start + end) // 2
        print(start, end, mid, self.get_copiers(pages, mid))
        if self.get_copiers(pages, mid) > k:
            start = mid
        else:
            end = mid

    if self.get_copiers(pages, start) <= k:
        return start
    return end


def get_copiers(self, pages, time):
    copiers = 0
    last_copied = time
    for page in pages:
        if page > time:
            return float('inf')

        if last_copied + page > time:
            copiers += 1
            last_copied = page
        else:
            last_copied += page

    return copiers


class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        if not pages or not k:
            return 0

        n = len(pages)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        for j in range(k + 1):
            dp[0][j] = 0

        prefixSum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + pages[i - 1]

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for prev in range(i):
                    cost = prefixSum[i] - prefixSum[prev]
                    dp[i][j] = min(dp[i][j], max(dp[prev][j - 1], cost))
                    # print(cost)
                    # print(dp)

        return dp[n][k]