class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        results = []
        self.dfs(s, 0, [], results)
        return results

    def dfs(self, s, start, res, results):
        if len(s) <= start:
            results.append(res[:])

        if start < len(s):
            res.append(s[start:start + 1])
            self.dfs(s, start + 1, res, results)
            res.pop()
        if start + 1 < len(s):
            res.append(s[start:start + 2])
            self.dfs(s, start + 2, res, results)
            res.pop()


class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, path, results):
        if s == "":
            results.append(path[:])
            return
        for i in range(2):
            if i + 1 <= len(s):
                path.append(s[:i + 1])
                self.dfs(s[i + 1:], path, results)
                path.pop()