class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        subset_sum = 0

        def backtracking(start: int, subset: List[int]):
            nonlocal subset_sum
            if subset_sum > n:
                return
            if len(subset) == k:
                if subset_sum == n:
                    res.append(subset[:])
                    return
                return

            for i in range(start, 10):
                subset.append(i)
                subset_sum += i
                backtracking(i + 1, subset)
                subset.pop()
                subset_sum -= i

        backtracking(1, [])

        return res
