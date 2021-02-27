class Solution:
    def findKthLargest(self,nums, k):
        left, right = 0 , len(nums)-1
        pivotIndex = self.partition(nums, left, right)
        while left<=right:
            pivotIndex = self.partition(nums, left, right)
            if pivotIndex == k-1:
                return nums[pivotIndex]
            elif pivotIndex > k-1:
                right = pivotIndex - 1
            else:
                left = pivotIndex+1
        return nums[k - 1]

    def partition(self, nums, start, end):
        pivotIndex = start
        pivot = nums[end]

        for i in range(start, end):
            if nums[i] > pivot:
                nums[pivotIndex], nums[i] = nums[i], nums[pivotIndex]
                pivotIndex += 1

        nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
        return pivotIndex



class Solution:
    def findKthLargest(self,nums, k):
        return sorted(nums)[len(nums)-k+1]
