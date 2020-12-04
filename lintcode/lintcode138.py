class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        prefix_hash = {0: -1}

        preifx_sum = 0
        for i, num in enumerate(nums):
            preifx_sum += num
            if preifx_sum in prefix_hash:
                return [prefix_hash[preifx_sum] + 1, i]

            prefix_hash[preifx_sum] = i

        return [-1, -1]