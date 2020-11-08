from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     return self.helper([], sorted(nums))
    #
    # def helper(self, cur, nums):
    #     if not nums:
    #         return [cur]
    #
    #     return self.helper(cur, nums[1:]) + self.helper(cur + [nums[0]], nums[1:])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            tmp = []
            for r in res:
                tmp.append(r)
                tmp.append(r + [num])
            res = tmp

        return res
