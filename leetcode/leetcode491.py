class Solution:
    def __init__(self):
        self.res = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.res.clear()
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums: List[int], start: int, tmp: List[int]):
        if len(tmp) > 1:
            self.res.append(tmp[:])

        used = set()
        for i in range(start, len(nums)):
            num = nums[i]
            if tmp and tmp[-1] > num:
                continue

            if num in used:
                continue

            used.add(num)
            tmp.append(num)
            self.dfs(nums, i + 1, tmp)
            tmp.pop()
            # no set.remove here, because 1 number can't be reused on the same level


class Solution:
    def __init__(self):
        self.res = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.res.clear()
        self.dfs(nums, 0, [])
        return self.res

    def dfs(self, nums: List[int], start: int, tmp: List[int]):
        if len(tmp) > 1:
            self.res.append(tmp[:])

        used = [False] * 201
        for i in range(start, len(nums)):
            num = nums[i]
            if tmp and tmp[-1] > num:
                continue

            if used[num + 100]:
                continue

            used[num + 100] = True
            tmp.append(num)
            self.dfs(nums, i + 1, tmp)
            tmp.pop()