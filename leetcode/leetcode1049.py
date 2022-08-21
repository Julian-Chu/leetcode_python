class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) //2

        dp = [0] * (target+1)

        for stone in stones:
            for i in range(target, stone-1, -1):
                dp[i] = max(dp[i], dp[i-stone] + stone)

        return sum(stones) - dp[target] * \
               2