class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        numbers.sort()

        res = []
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            num = numbers[i]
            start, end = i + 1, len(numbers) - 1
            used = {}

            while start < end:
                if start < end and numbers[start] + numbers[end] + num > 0:
                    end -= 1
                elif start < end and numbers[start] + numbers[end] + num < 0:
                    start += 1
                else:
                    if numbers[start] not in used:
                        res.append([num, numbers[start], numbers[end]])
                        used[numbers[start]] = True
                        used[numbers[end]] = True
                    start += 1
                    end -= 1

        return res


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        numbers.sort()

        res = []
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            num = numbers[i]
            start, end = i + 1, len(numbers) - 1

            while start < end:
                #  remove duplicate
                if start > i + 1 and numbers[start] == numbers[start - 1]:
                    start += 1
                    continue

                if start < end and numbers[start] + numbers[end] + num > 0:
                    end -= 1
                elif start < end and numbers[start] + numbers[end] + num < 0:
                    start += 1
                else:
                    res.append([num, numbers[start], numbers[end]])
                    start += 1
                    end -= 1

        return res


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        nums = sorted(numbers)

        results = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], results)

        return results

    def find_two_sum(self, nums, left, right, target, results):
        last_pair = None
        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    results.append([-target, nums[left], nums[right]])
                last_pair = (nums[left], nums[right])
                right -= 1
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1



