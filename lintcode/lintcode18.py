class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        if not nums:
            return [[]]
        nums.sort()
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, index, subset, subsets):
        subsets.append(list(subset))

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()


class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        if not nums:
            return [[]]
        nums.sort()
        subsets = []
        self.dfs(nums, 0, -1, [], subsets)
        return subsets

    def dfs(self, nums, index, lastSelectedIndex, subset, subsets):
        if index == len(nums):
            subsets.append(subset[:])
            return

        self.dfs(nums, index + 1, lastSelectedIndex, subset, subsets)

        if index > 0 and nums[index] == nums[index - 1] and index - 1 != lastSelectedIndex:
            return

        subset.append(nums[index])
        self.dfs(nums, index + 1, index, subset, subsets)
        subset.pop()