class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 != 0:
            return False
        _sum = sum(nums) // 2

        dp = [[0] * (_sum+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(_sum+1):
                if j >= nums[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1] == _sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 != 0:
            return False
        _sum = sum(nums) // 2

        dp = [0] * (_sum+1)

        for num in nums:
            for j in range(_sum, num-1, -1):
                dp[j] = max(dp[j], dp[j-num] + num)

        return dp[_sum] == _sum