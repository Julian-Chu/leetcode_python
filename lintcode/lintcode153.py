class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        if not num:
            return []
        results = []
        num.sort()
        self.dfs(num, 0, [], results, target)
        return results

    def dfs(self, nums, index, comb, results, target):
        if target == 0:
            results.append(comb[:])
            return

        if index == len(nums):
            return

        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            if i > index and nums[i - 1] == nums[i]:
                continue

            comb.append(nums[i])
            self.dfs(nums, i + 1, comb, results, target - nums[i])
            comb.pop()