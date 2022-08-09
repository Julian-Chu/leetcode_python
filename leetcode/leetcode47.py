class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
        self.used = set()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()

        self.dfs(nums)
        return self.res

    def dfs(self, nums):
        if len(self.tmp) == len(nums):
            self.res.append(self.tmp[:])
            return

        for i in range(len(nums)):
            if i in self.used:
                continue

            if i > 0 and nums[i] == nums[i - 1] and (i - 1 not in self.used):
                continue

            self.used.add(i)
            self.tmp.append(nums[i])
            self.dfs(nums)
            self.tmp.pop()
            self.used.remove(i)


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()

        res = []
        used = [False] * len(nums)

        def backtracking(nums, used, path):
            if len(nums) == len(path):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtracking(nums, used, path)
                path.pop()
                used[i] = False

        backtracking(nums, used, [])

        return res