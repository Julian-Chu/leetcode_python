class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """

    def kthLargestElement2(self, nums, k):
        if not nums:
            return None
        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, start, end, n):
        if start >= end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if n <= right:
            return self.partition(nums, start, right, n)
        if n >= left:
            return self.partition(nums, left, end, n)
        return nums[n]