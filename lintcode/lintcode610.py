"""
O(n)
"""
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """

    def twoSum7(self, nums, target):
        n = len(nums)
        if target < 0:
            target = -target
        j = 1
        for i in range(n):
            j = max(j, i + 1)
            while j < n and nums[j] - nums[i] < target:
                j += 1
            if j >= n:
                break
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]

        return [-1, -1]


# ~= nlogn
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        if not nums:
            return []

        for i in range(len(nums ) -1):
            val = abs(target) + nums[i]
            index = self.binary_search(nums, i+ 1, val)
            if index is None:
                continue
            return [nums[i], nums[index]]

        return []

    def binary_search(self, nums, index, target):
        start, end = index, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                return mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return None