class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here

        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            res = max(res, dp[i])

        return res


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        prefix_sum = 0
        max_sum, min_sum = -float('inf'), 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum