from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if k == 0 or k == n:
            return
        k %= n
        self.rev(nums, 0, n - 1)
        self.rev(nums, 0, k - 1)
        self.rev(nums, k, n - 1)

    def rev(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
