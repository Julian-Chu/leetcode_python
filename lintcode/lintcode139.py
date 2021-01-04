class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        prefix_sum = [(0, -1)]
        for i, num in enumerate(nums):
            prefix_sum.append((prefix_sum[-1][0] + num, i))

        prefix_sum.sort()

        closet, answer = float('inf'), []
        for i in range(1, len(prefix_sum)):
            if closet > prefix_sum[i][0] - prefix_sum[i - 1][0]:
                closet = prefix_sum[i][0] - prefix_sum[i - 1][0]
                left = min(prefix_sum[i - 1][1], prefix_sum[i][1]) + 1  # prefix
                right = max(prefix_sum[i - 1][1], prefix_sum[i][1])
                answer = [left, right]
        return answer
    
"""
time limit exceed
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        if not nums:
            return []
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        min_sum = float('inf')
        res = [0, 0]
        for i in range(n):
            for j in range(i, n):
                tmp = abs(prefix_sum[j + 1] - prefix_sum[i])
                if min_sum > tmp:
                    min_sum = tmp
                    res = [i, j]
                    if tmp == 0:
                        return res

        return res