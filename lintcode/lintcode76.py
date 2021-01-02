"""
n^2
"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        n = len(nums)

        # state
        dp = [1] * n
        max_length = 1
        for i in range(n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_length:
                        max_length = dp[i]

        return max_length

"""
dp path
"""


class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0

        # state: dp[i] 表示从左到右跳到i的最长sequence 的长度

        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)

        # prev[i] 代表 dp[i] 的最优值是从哪个 dp[j] 算过来的
        prev = [-1] * len(nums)

        # function dp[i] = max{dp[j] + 1},  j < i and nums[j] < nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # answer: max(dp[0..n-1])
        longest, last = 0, -1
        for i in range(len(nums)):
            if dp[i] > longest:
                longest = dp[i]
                last = i

        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        print(path[::-1])

        return longest
"""
nlog(n)
"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        n = len(nums)

        lis = [float('inf')] * (n + 1)
        lis[0] = - float('inf')
        longest = 0
        for num in nums:
            index = self.get_index(lis, num)
            lis[index] = num
            longest = max(longest, index)
        print(lis[1:1+longest]) # path
        return longest

    def get_index(self, nums, target):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start

        return end


