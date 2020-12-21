class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        if not nums:
            return [[]]

        queue = [[]]

        for num in sorted(nums):
            for i in range(len(queue)):
                queue.append(queue[i] + [num])

        return queue

class Solution:
    def subsets(self, nums):
        if not nums:
            return [[]]

        queue = [[]]
        index = 0
        while index < len(queue):
            subset = queue[index]
            index += 1
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])

        return queue