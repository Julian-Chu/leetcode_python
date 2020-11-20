class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        start, end = 0, len(nums) - 1
        unique_pairs = 0
        while start < end:
            sum = nums[start] + nums[end]

            if sum == target:
                while start + 1 < end and nums[start] == nums[start + 1]:
                    start += 1
                while start + 1 < end and nums[end] == nums[end - 1]:
                    end -= 1
                unique_pairs += 1
                start += 1
                end -= 1
            elif sum > target:
                end -= 1
            else:
                start += 1

        return unique_pairs

class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        used = {}
        pairs = 0
        for num in nums:
            if target - num in used and used[target - num] == False:
                pairs += 1
                used[target - num] = True
                used[num] = True

            if num not in used:
                used[num] = False

        return pairs