class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if not nums:
            return [[]]

        results = []
        visited = set()
        permutationSet = set()
        nums.sort();
        self.dfs(nums, visited, [], permutationSet, results)
        return results

    def dfs(self, nums, visited, permutation, permutationSet, results):
        if len(permutation) == len(nums):
            key = self.getPermutationKey(permutation)
            if key not in permutationSet:
                results.append(list(permutation))
                permutationSet.add(key)
            return

        for i in range(len(nums)):
            if i in visited:
                continue
            visited.add(i)
            permutation.append(nums[i])
            self.dfs(nums, visited, permutation, permutationSet, results)
            visited.remove(i)
            permutation.pop(-1);

    def getPermutationKey(self, permutation):
        if not permutation:
            return ""
        return "-".join(str(num) for num in permutation)