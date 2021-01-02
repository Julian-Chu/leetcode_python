class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        if not costs:
            return 0

        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]

        for j in range(3):
            dp[0][j] = costs[0][j]

        for i in range(1, n):
            for j in range(3):
                dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + costs[i][j]

        return min(dp[n - 1])


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        if not costs:
            return 0

        n = len(costs)
        dp = [[0] * 3 for _ in range(2)]

        for j in range(3):
            dp[0][j] = costs[0][j]

        for i in range(1, n):
            for j in range(3):
                dp[i % 2][j] = min(dp[(i - 1) % 2][(j + 1) % 3], dp[(i - 1) % 2][(j + 2) % 3]) + costs[i][j]

        return min(dp[(n - 1) % 2])


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, costs):
        r, b, g = 0, 0, 0

        for r_cost, b_cost, g_cost in costs:
            r, b, g = r_cost + min(b, g), b_cost + min(r, g), g_cost + min(r, b)

        return min(r, b, g)