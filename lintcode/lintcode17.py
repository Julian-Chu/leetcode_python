
class Solution:
    def subsets(self, nums):
        if not nums:
            return [[]]
        combinations = []
        self.dfs(sorted(nums), 0, [], combinations)
        return combinations


    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()


class Solution:
    def subsets(self, nums):
        if not nums:
            return [[]]
        n = len(nums)
        nums.sort()
        results = []
        # all combination
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j) != 0:
                    subset.append(nums[j])
            results.append(subset)
        return results


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