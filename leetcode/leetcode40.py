class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
        self.cur_sum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        self.res.clear()
        self.tmp.clear()
        self.cur_sum = 0
        used = [False] * len(candidates)

        self.backtracking(candidates, 0, target, used)
        return self.res

    def backtracking(self, candidates, start_index, target, used):
        if self.cur_sum == target:
            self.res.append(self.tmp[:])
            return

        for i in range(start_index, len(candidates)):
            num = candidates[i]
            if self.cur_sum + num > target:
                return
            if i > 0 and candidates[i] == candidates[i - 1] and not used[i - 1]:
                continue
            self.tmp.append(num)
            self.cur_sum += num
            used[i] = True
            self.backtracking(candidates, i + 1, target, used)
            used[i] = False
            self.cur_sum -= num
            self.tmp.pop()


class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
        self.cur_sum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        self.res.clear()
        self.tmp.clear()
        self.cur_sum = 0

        self.backtracking(candidates, 0, target)
        return self.res

    def backtracking(self, candidates, start_index, target):
        if self.cur_sum == target:
            self.res.append(self.tmp[:])
            return

        for i in range(start_index, len(candidates)):
            num = candidates[i]
            if self.cur_sum + num > target:
                return
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
            self.tmp.append(num)
            self.cur_sum += num
            self.backtracking(candidates, i + 1, target)
            self.cur_sum -= num
            self.tmp.pop()