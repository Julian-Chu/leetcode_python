class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """

    def twoSum2(self, nums, target):
        if not nums:
            return 0

        n = len(nums)
        if n < 2:
            return 0

        nums.sort()
        ans = 0

        l, r = 0, n - 1

        while l < r:
            if nums[l] + nums[r] <= target:
                l += 1
            else:
                ans += r - l  # l to r-1, 都可以跟r組成pair
                r -= 1

        return ans
