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


class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        res = []
        finished = nums[:]
        nums = self.nextPermutation(nums)
        while nums != finished:
            res.append(nums[:])
            nums = self.nextPermutation(nums)

        res.append(finished[:])
        return res

    def nextPermutation(self, nums):
        if len(nums) < 2:
            return nums

        n = len(nums)
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i != 0:
            j = n - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
        self.swapList(nums, i, n - 1)

        return nums

    def swapList(self, nums, start, end):
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1