"""
bad
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        if not numbers:
            return 0

        numbers.sort()
        sum3_closest = float('inf')
        for i in range(len(numbers) - 2):
            for j in range(i + 1, len(numbers) - 1):
                temp_target = target - numbers[i] - numbers[j]
                k = self.binary_search(numbers, j + 1, len(numbers) - 1, temp_target)
                sum3 = numbers[i] + numbers[j] + numbers[k]

                if abs(sum3_closest - target) > abs(sum3 - target):
                    sum3_closest = sum3

        return sum3_closest

    def binary_search(self, numbers, start, end, target):
        if start >= end:
            return start

        while start + 1 < end:
            mid = (start + end) // 2
            if numbers[mid] < target:
                start = mid
            elif numbers[mid] > target:
                end = mid
            else:
                return mid

        if abs(numbers[start] - target) < abs(numbers[end] - target):
            return start
        return end

"""
binary search
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        if not numbers:
            return 0
        numbers.sort()
        ans = None
        for i in range(len(numbers) - 2):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                sum3 = numbers[i] + numbers[left] + numbers[right]
                if ans is None or abs(target - ans) > abs(target - sum3):
                    ans = sum3

                if target > sum3:
                    left += 1
                elif target < sum3:
                    right -= 1
                else:
                    return target

        return ans



