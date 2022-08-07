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


class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        self.dfs(nums, 0)
        return self.res

    def dfs(self, nums: List[int], start_index: int):
        self.res.append(self.tmp[:])
        if start_index >= len(nums):
            return

        for i in range(start_index, len(nums)):
            num = nums[i]
            self.tmp.append(num)
            self.dfs(nums, i + 1)
            self.tmp.pop()