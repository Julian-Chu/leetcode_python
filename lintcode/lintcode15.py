class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if not nums:
            return [[]]

        queue = collections.deque()

        for num in nums:
            queue.append([num])
        result = []
        while queue:
            permutation = queue.popleft()
            if len(permutation) == len(nums):
                result.append(permutation)
                continue

            for num in nums:
                if num in permutation:
                    continue
                next_p = permutation[:]
                next_p.append(num)
                queue.append(next_p)
        return result


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


class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if not nums:
            return [[]]

        permutations = []
        self.dfs(sorted(nums), set(), [], permutations)
        return permutations

    def dfs(self, nums, visited, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return

        for i, num in enumerate(nums):
            if i in visited:
                continue
            if i > 0 and nums[i - 1] == nums[i] and (i - 1 not in visited):
                continue
            permutation.append(num)
            visited.add(i)
            self.dfs(nums, visited, permutation, permutations)
            visited.remove(i)
            permutation.pop()