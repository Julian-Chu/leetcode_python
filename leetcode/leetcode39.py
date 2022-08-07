class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
        self.cur_sum = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target <= 0:
            return []

        candidates.sort()
        self.dfs(candidates, target, 0)
        return self.res

    def dfs(self, candidates, target, start_index):
        if self.cur_sum == target:
            self.res.append(self.tmp[:])
            return

        for idx in range(start_index, len(candidates)):
            if idx < start_index:
                continue
            num = candidates[idx]
            if self.cur_sum + num > target:
                return
            self.cur_sum += num
            self.tmp.append(num)
            self.dfs(candidates, target, idx)
            self.tmp.pop()
            self.cur_sum -= num