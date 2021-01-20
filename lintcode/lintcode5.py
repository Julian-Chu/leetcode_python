class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        return self.partition(n, nums, 0, len(nums) - 1)

    def partition(self, n, nums, start, end):
        if start >= end:
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
            return self.partition(n, nums, start, right)
        if n - 1 >= left:
            return self.partition(n, nums, left, end)

        return nums[right + 1]


class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        left, right = 0 , len(nums)-1
        pivotIndex = self.partition(nums, left, right)
        while left<=right:
            pivotIndex = self.partition(nums, left, right)
            if pivotIndex == n-1:
                return nums[pivotIndex]
            elif pivotIndex > n-1:
                right = pivotIndex - 1
            else:
                left = pivotIndex+1
        return nums[n-1]

    def partition(self, nums, start, end):
        pivotIndex = start
        pivot = nums[end]

        for i in range(start, end):
            if nums[i] > pivot:
                nums[pivotIndex], nums[i] = nums[i], nums[pivotIndex]
                pivotIndex += 1

        nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
        return pivotIndex
