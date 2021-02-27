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
