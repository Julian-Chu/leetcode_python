class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = nums[0]
        _sum = nums[0]
        for i in range(1, len(nums)):
            _sum += nums[i]
            if _sum < nums[i]:
                _sum = nums[i]

            if _sum > res:
                res = _sum

        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            if dp[i] > res:
                res = dp[i]

        return res
