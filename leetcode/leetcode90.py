from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.helper(res, nums, [], 0)
        return res

    def helper(self, res, nums, cur, idx):
        res.append(cur[:])

        for i in range(idx, len(nums)):
            if i == idx or nums[i] != nums[i - 1]:
                self.helper(res, nums, cur + [nums[i]], i + 1)


class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.res.clear()
        self.tmp.clear()
        nums.sort()
        self.dfs(nums, 0)
        return self.res

    def dfs(self, nums: List[int], start_index: int):
        self.res.append(self.tmp[:])
        if start_index == len(nums):
            return

        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue

            self.tmp.append(nums[i])
            self.dfs(nums, i + 1)
            self.tmp.pop()