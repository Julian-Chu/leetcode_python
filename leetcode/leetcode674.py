class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        slow = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                slow = i

            ans = max(ans, i-slow+1)
        return ans

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        result = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = max(dp[i], dp[i-1]+1)
            result = max(result, dp[i])

        return result