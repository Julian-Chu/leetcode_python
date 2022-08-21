class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        _sum = sum(nums)

        if abs(target) > _sum:
            return 0

        if (target + _sum) % 2 == 1:
            return 0

        bagsize = (target + _sum) // 2
        dp = [0] * (bagsize+1)
        dp[0] = 1
        for num in nums:
            for i in range(bagsize, num-1, -1):
                dp[i] += dp[i-num]
        return dp[bagsize]