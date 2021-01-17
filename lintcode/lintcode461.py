class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        return self.find_kth(nums, 0, len(nums) - 1, k - 1)

    def find_kth(self, nums, start, end, k):
        if start >= end:
            return nums[k]

        left, right = start, end

        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1
        if k <= right:
            return self.find_kth(nums, start, right, k)
        elif k >= left:
            return self.find_kth(nums, left, end, k)

        return nums[k]