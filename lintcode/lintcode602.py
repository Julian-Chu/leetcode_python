
"""
O(nlogn)
"""
class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0

        lis = [float('inf')] * (len(envelopes) + 1)
        lis[0] = -float('inf')

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        longest = 0
        for (_, h) in envelopes:
            index = self.get_first_gte(lis, h)
            lis[index] = h
            longest = max(longest, index)

        return longest

    def get_first_gte(self, nums, target):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return start
        return end
"""
O(n^2) : timeout
"""
class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        # write your code here

        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], x[1]))
        n = len(envelopes)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if self.can_fit(envelopes, i, j):
                    print(i, j)
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def can_fit(self, envelopes, i, j):
        return envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]

