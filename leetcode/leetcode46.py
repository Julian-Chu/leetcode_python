class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
        self.used = set()

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.res.clear()
        self.tmp.clear()
        self.used.clear()
        self.dfs(nums)
        return self.res

    def dfs(self, nums):
        if len(self.tmp) == len(nums):
            self.res.append(self.tmp[:])
            return

        for i in range(len(nums)):
            if nums[i] in self.used:
                continue

            self.used.add(nums[i])
            self.tmp.append(nums[i])
            self.dfs(nums)
            self.tmp.pop()
            self.used.remove(nums[i])