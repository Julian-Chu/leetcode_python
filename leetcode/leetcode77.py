class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []

        path = []
        res = []

        def dfs(n: int, k: int, start: int):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                dfs(n, k, i + 1)
                path.pop()

        dfs(n, k, 1)
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []

        path = []
        res = []

        def dfs(n: int, k: int, start: int):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                dfs(n, k, i + 1)
                path.pop()

        dfs(n, k, 1)
        return res
