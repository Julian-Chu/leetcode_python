class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        if len(numbers) < 2:
            return [-1, -1]
        value_index_map = {}
        for index, num in enumerate(numbers):
            key = target - num
            if key in value_index_map:
                return [value_index_map[key], index]
            value_index_map[num] = index

        return [-1, -1]

    def twoSum(self, numbers, target):
        if len(numbers) < 2:
            return [-1, -1]
        rec = dict()
        for i, num in enumerate(numbers):
            key = target - num
            if key in rec:
                return [rec[key], i]
            rec[num] = i

        return [-1, -1]
