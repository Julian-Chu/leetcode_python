class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        if not numbers:
            return []
        numbers.sort()
        n = len(numbers)
        result = []
        for i in range(n):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    if left > j + 1 and numbers[left] == numbers[left - 1]:
                        left += 1
                        continue
                    if right < n - 1 and numbers[right] == numbers[right + 1]:
                        right -= 1
                        continue

                    val = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                    if val == target:
                        result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left += 1
                        right -= 1
                    elif val > target:
                        right -= 1
                    else:
                        left += 1
        return result


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        if not numbers:
            return []
        numbers.sort()
        n = len(numbers)
        result = []
        for i in range(n):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                pairs = self.find_two_sum_pairs(
                    numbers,
                    j + 1,
                    len(numbers) - 1,
                    target - numbers[i] - numbers[j],
                )

                for (c, d) in pairs:
                    result.append([numbers[i], numbers[j], c, d])

        return result

    def find_two_sum_pairs(self, nums, left, right, target):
        pairs = []
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                if not pairs or (nums[left], nums[right]) != pairs[-1]:
                    pairs.append((nums[left], nums[right]))
                left += 1
                right -= 1
        return pairs