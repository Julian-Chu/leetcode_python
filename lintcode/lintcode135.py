class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        combinations = []
        self.dfs(sorted(candidates), 0, [], target, combinations)
        return combinations

    def dfs(self, candidates, index, combination, target, combinations):
        if target == 0:
            combinations.append(combination[:])
            return

        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break  # prunning, because candidate is inorder
            if i > 0 and candidates[i - 1] == candidates[i]:
                continue
            combination.append(candidates[i])
            self.dfs(candidates, i, combination, target - candidates[i], combinations)
            combination.pop()


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates, target, start, combination, results):
        if target < 0:
            return
        if target == 0:
            results.append(list(combination))
            return

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            combination.pop()