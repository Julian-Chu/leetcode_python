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


class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, num, target):
        num.sort()
        result = []
        visited = set()
        for i in range(len(num)):
            if i > 0 and num[i - 1] == num[i] and (i - 1) not in visited:
                continue
            visited.add(i)
            self.dfs(num, i, [num[i]], result, target - num[i], visited)
            visited.remove(i)

        return result

    def dfs(self, num, start, res, result, target, visited):
        if target == 0:
            result.append(res[:])
            return

        if target < 0:
            return

        for i in range(start + 1, len(num)):
            if num[i - 1] == num[i] and (i - 1) not in visited:
                continue
            res.append(num[i])
            visited.add(i)
            self.dfs(num, i, res, result, target - num[i], visited)
            visited.remove(i)
            res.pop()


