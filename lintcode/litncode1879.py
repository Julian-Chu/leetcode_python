class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """

    def twoSumVII(self, nums, target):
        n = len(nums)
        if n < 2:
            return []

        right = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] > nums[right]:
                right = i
            if nums[i] < nums[left]:
                left = i

        ans = []
        while (nums[left] < nums[right]):
            print(left, right)
            if nums[left] + nums[right] < target:
                left = self.find_larger_left(nums, left)
            elif nums[left] + nums[right] > target:
                right = self.find_smaller_right(nums, right)
            else:
                if left < right:
                    ans.append([left, right])
                else:
                    ans.append([right, left])
                left = self.find_larger_left(nums, left)
                right = self.find_smaller_right(nums, right)

        return ans

    def find_smaller_right(self, nums, right):
        n = len(nums)
        if nums[right] > 0:
            for i in range(right - 1, -1, -1):
                if nums[i] > 0:
                    return i
            # all numbers smaller than right is negative
            for i in range(n):
                if nums[i] <= 0:
                    return i
            return -1
        for i in range(right + 1, n):
            if nums[i] <= 0:
                return i
        return -1

    def find_larger_left(self, nums, left):
        n = len(nums)
        if nums[left] < 0:
            for i in range(left - 1, -1, -1):
                if nums[i] < 0:
                    return i
            for i in range(n):
                if nums[i] > 0:
                    return i
            return -1
        for i in range(left + 1, n):
            if nums[i] > 0:
                return i
        return -1