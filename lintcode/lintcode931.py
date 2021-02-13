class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """

    def findMedian(self, nums):
        if not nums:
            return 0.0

        n = sum(len(arr) for arr in nums)
        if n == 0:
            return 0.0

        if n % 2 == 1:
            return self.find_kth(nums, n // 2 + 1) * 1.0
        return (self.find_kth(nums, n // 2) + self.find_kth(nums, n // 2 + 1)) / 2.0

    def find_kth(self, arrs, k):
        start, end = self.get_range(arrs)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_smaller_or_equal(arrs, mid) >= k:
                end = mid
            else:
                start = mid

        if self.get_smaller_or_equal(arrs, start) >= k:
            return start
        return end

    def get_range(self, arrs):
        start = min(arr[0] for arr in arrs if len(arr))
        end = max(arr[-1] for arr in arrs if len(arr))
        return start, end

    def get_smaller_or_equal(self, arrs, val):
        count = 0
        for arr in arrs:
            # timout
            # count += len([e for e in arr if e<=val]):
            count += self.get_smaller_or_equal_in_arr(arr, val)
        return count

    def get_smaller_or_equal_in_arr(self, arr, val):
        if not arr:
            return 0
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] > val:
                end = mid
            else:
                start = mid

        if arr[start] > val:
            return start
        if arr[end] > val:
            return end
        # arr所有元素小於val的狀況
        return end + 1


"""
TLE
"""
import heapq


class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """

    def findMedian(self, nums):
        if not nums:
            return 0

        n = sum([len(num) for num in nums])
        if n == 0:
            return 0.00
        merged = self.mergeToMedian(nums)
        if n % 2 == 1:
            return merged[n // 2]

        return (merged[n // 2 - 1] + merged[n // 2]) / 2

    def mergeToMedian(self, nums):
        n = sum([len(num) for num in nums])
        median = n // 2 + 1
        res = []

        heap = []
        for i, num in enumerate(nums):
            if len(num) == 0:
                continue
            heapq.heappush(heap, (num[0], i, 0))

        for _ in range(median):
            n, arrs_index, arr_index = heapq.heappop(heap)
            res.append(n)

            if arr_index + 1 < len(nums[arrs_index]):
                heapq.heappush(heap, (nums[arrs_index][arr_index + 1], arrs_index, arr_index + 1))

        return res