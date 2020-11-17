class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        if len(nums) <=1:
            return 0
        nums.sort()
        left, right = 0, len(nums) - 1

        count = 0
        while left < right:
            while left < right and nums[left] + nums[right] > target:
                right -= 1

            count += right - left
            left += 1
        return count
