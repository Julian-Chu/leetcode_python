class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        if not numbers:
            return []

        numToIndex = {}

        for i, num in enumerate(numbers):
            val = target - num
            if val not in numToIndex:
                numToIndex[num] = i
            else:
                return [numToIndex[val], i]
        return []


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        if not numbers:
            return []

        nums = [(num, i) for (i, num) in enumerate(numbers)]
        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l][0] + nums[r][0] > target:
                r -= 1
            elif nums[l][0] + nums[r][0] < target:
                l += 1
            else:
                return sorted([nums[l][1], nums[r][1]])
        return [-1, -1]