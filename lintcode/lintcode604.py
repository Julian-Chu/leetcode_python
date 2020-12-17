class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        if not nums:
            return []

        if len(nums) <= k:
            return [sum(nums)]

        results = []

        n = len(nums)
        left = 0
        sum_in_window = 0
        for right in range(n):
            sum_in_window += nums[right]
            while right - left > k:
                left += 1

            if right < k:
                if right == k - 1:
                    results.append(sum_in_window)
                continue
            sum_in_window -= nums[left]
            results.append(sum_in_window)

        return results


class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        if not nums or len(nums) < k:
            return []

        n = len(nums)

        result = []
        j, window_sum = 0, 0
        for i in range(n):
            while j < n and j - i < k:
                window_sum += nums[j]
                j += 1

            if j - i == k:
                result.append(window_sum)
            window_sum -= nums[i]

        return result