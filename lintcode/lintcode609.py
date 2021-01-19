"""
two pointer: O(n)
"""
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
"""
binary search
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        if not nums:
            return 0
        nums.sort()
        n=len(nums)
        count = 0
        for i in range(n):
            start, end = i, n-1
            while start +1 < end:
                mid = (start+end)//2
                if nums[mid] > target - nums[i]:
                    end = mid
                else:
                    start = mid
            if nums[end] <= target - nums[i]:
                count += end - i
            else:
                count += start -i
        return count

"""
暴力枚舉: O(n^2)
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """

    def twoSum5(self, nums, target):
        if not nums:
            return 0

        nums.sort()
        pairs = 0
        n = len(nums)

        for i in range(n):
            j = n - 1
            while i < j:
                if nums[i] + nums[j] > target:
                    j -= 1
                else:
                    break
            pairs += j - i

        return pairs
