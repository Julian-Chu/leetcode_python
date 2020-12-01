class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if not nums:
            # 0!=1
            # 1!=1
            # 2!=2
            return [[]]
        permutations = []
        self.dfs(nums, set(), [], permutations)
        return permutations

    # 遞歸的定義:找到所有permutation開頭的permutations
    def dfs(self, nums, visited, permutation, permutations):
        # 遞歸的出口
        if len(nums) == len(permutation):
            permutations.append(list(permutation)) # deep copy
            return

        # 遞歸的拆解
        # [] -> [1], [2], [3]
        # [1] -> [1,2], [1,3]
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            self.dfs(nums, visited, permutation, permutations)
            visited.remove(num)
            permutation.pop()
