class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        return self.quickselect(n, nums, 0, len(nums) - 1)

    def quickselect(self, n, nums, start, end):

        if start == end:
            return nums[start]
        # pivotIndex = int(start + (end - start) / 2)

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if n - 1 <= right:
            return self.quickselect(n, nums, start, right)
        if n - 1 >= left:
            return self.quickselect(n, nums, left, end)

        return nums[right + 1]