class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        if len(s) == 1:
            return [[s]]

        self.dfs(s, 0)
        return self.res

    def dfs(self, s: str, start_index: int):
        if start_index == len(s):
            self.res.append(self.tmp[:])
            return

        for end in range(start_index, len(s)):
            if not self.isPalindrome(s[start_index:end + 1]):
                continue

            self.tmp.append(s[start_index:end + 1])
            self.dfs(s, end + 1)
            self.tmp.pop()

    def isPalindrome(self, s: str):
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
        self.memo = {}

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        if len(s) == 1:
            return [[s]]

        self.dfs(s, 0)
        return self.res

    def dfs(self, s: str, start_index: int):
        if start_index == len(s):
            self.res.append(self.tmp[:])
            return

        for end in range(start_index, len(s)):
            if not self.isPalindrome(s, start_index, end):
                continue

            self.tmp.append(s[start_index:end + 1])
            self.dfs(s, end + 1)
            self.tmp.pop()

    def isPalindrome(self, s: str, start: int, end: int):
        key = (start, end)
        if self.memo.get(key, None) is not None:
            return self.memo.get(key)
        l, r = start, end

        while l < r:
            if s[l] != s[r]:
                self.memo[key] = False
                return self.memo[key]
            l += 1
            r -= 1
        self.memo[key] = True
        return self.memo[key]


class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
        self.memo = {}

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        if len(s) == 1:
            return [[s]]

        self.dfs(s, 0)
        return self.res

    def dfs(self, s: str, start_index: int):
        if start_index == len(s):
            self.res.append(self.tmp[:])
            return

        for end in range(start_index, len(s)):
            str_ = s[start_index:end + 1]
            if str_ != str_[::-1]:
                continue

            self.tmp.append(s[start_index:end + 1])
            self.dfs(s, end + 1)
            self.tmp.pop()