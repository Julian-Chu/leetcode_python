class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):

        idx = 0
        n = len(colors)
        for target in range(1, k):
            idx = self.partition(colors, idx, target)

    def partition(self, nums, start, target):
        l, r = start, len(nums) - 1

        while l <= r:
            while l <= r and nums[l] <= target:
                l += 1
            while l <= r and nums[r] > target:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return l

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        start = 0
        for target in range(2, k + 1):
            start = self.partition(colors, start, target)

    def partition(self, colors, start, target):
        left, right = start, len(colors) - 1
        while left <= right:
            while left <= right and colors[left] < target:
                left += 1
            while left <= right and colors[right] >= target:
                right -= 1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        return left

# 通用quicksort
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        self.quicksort(colors, 0, len(colors) - 1)

    def quicksort(self, colors, start, end):
        print(start, end)
        if start >= end:
            return

        l, r = start, end
        pivot = colors[(start + end) // 2]
        while l <= r:
            # colors[l] < pivot not colors[l] <= pivot
            while l <= r and colors[l] < pivot:
                l += 1
            while l <= r and colors[r] > pivot:
                r -= 1
            if l <= r:
                colors[l], colors[r] = colors[r], colors[l]
                l += 1
                r -= 1

        self.quicksort(colors, start, r)
        self.quicksort(colors, l, end)

# 對colors特化，雙重quicksort
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        self.quicksort(colors, 1, k, 0, len(colors) - 1)

    def quicksort(self, colors, color_start, color_end, start, end):
        if color_start >= color_end or start >= end:
            return

        color = color_start + (color_end - color_start) // 2
        left, right = start, end

        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.quicksort(colors, color_start, color, start, right)
        self.quicksort(colors, color + 1, color_end, left, end)