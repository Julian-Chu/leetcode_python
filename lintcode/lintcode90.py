class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        if not A:
            return []
        A = sorted(A)
        subsets = []
        self.dfs(A, 0, k, target, [], subsets)
        return subsets

    def dfs(self, A, index, k, target, subset, subsets):
        if k == 0 and target == 0:
            subsets.append(list(subset))
            return

        if k == 0 or target <= 0:
            return

        for i in range(index, len(A)):
            subset.append(A[i])
            self.dfs(A, i + 1, k - 1, target - A[i], subset, subsets)
            subset.pop()


class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        if not A:
            return []
        A.sort()

        result = []
        combination = []
        self.dfs(A, 0, combination, k, target, result)
        return result

    def dfs(self, nums, index, combination, k, target, result):
        if k == 0:
            if target == 0:
                result.append(combination[:])
            return
        if target <= 0:
            return
        if index == len(nums):
            return

        combination.append(nums[index])
        self.dfs(nums, index + 1, combination, k - 1, target - nums[index], result)
        combination.pop()
        self.dfs(nums, index + 1, combination, k, target, result)