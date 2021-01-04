class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """

    def canCross(self, stones):
        # write your code here
        if not stones:
            return False

        dp = {}
        for stone in stones:
            dp[stone] = set()

        dp[0].add(1)

        for stone in stones:
            last_steps = dp[stone]

            for k in last_steps:
                if k > 1 and k - 1 + stone in dp:
                    dp[stone + k - 1].add(k - 1)

                if stone + k in dp:
                    dp[stone + k].add(k)

                if stone + k + 1 in dp:
                    dp[stone + k + 1].add(k + 1)

        return len(dp[stones[-1]]) > 0
