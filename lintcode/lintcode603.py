"""
TLE O(n^2)
"""
class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums = sorted(nums)
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        last = -1
        longest = 0
        for i in range(n):
            if dp[i] > longest:
                longest = dp[i]
                last = i
        res = []
        while last != -1:
            res.append(nums[last])
            last = prev[last]
        return res

"""
dp只需要限制在nums的elements，
針對每個num取得factors，  **怎麼取得factors
在檢查factors是否在dp, 後在function去update
O( n * sqrt(n))
"""
class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums = sorted(nums)
        n = len(nums)
        dp, prev = {}, {}

        for num in nums:
            dp[num] = 1
            prev[num] = -1

        last_num = nums[0]
        for num in nums:
            for factor in self.get_smaller_factors(num):
                if factor not in dp:
                    continue
                if dp[num] < dp[factor] + 1:
                    dp[num] = dp[factor] + 1
                    prev[num] = factor

                if dp[num] > dp[last_num]:
                    last_num = num

        return self.get_path(prev, last_num)

    def get_path(self, prev, last_num):
        path = []
        while last_num != -1:
            path.append(last_num)
            last_num = prev[last_num]
        return path[::-1]

    def get_smaller_factors(self, num):
        if num == 1:
            return []
        factor = 1
        factors = []
        while factor * factor <= num:
            if num % factor == 0:
                factors.append(factor)
                if factor * factor != num and factor != 1:
                    factors.append(num // factor)
            factor += 1
        return factors




