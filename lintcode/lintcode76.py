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


