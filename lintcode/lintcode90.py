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

