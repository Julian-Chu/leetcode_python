class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    def findMin(self, nums):
        max = nums[0]
        maxIndex = 0

        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
                maxIndex = i

        if maxIndex == len(nums) - 1:
            return nums[0]
        else:
            return nums[maxIndex + 1]