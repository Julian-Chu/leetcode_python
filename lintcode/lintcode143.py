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