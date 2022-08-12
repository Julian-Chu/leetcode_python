class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)

    def helper(self, s: str) -> str:
        str_ = ""

        for i in range(len(s)):
            if s[i] == '#':
                if len(str_) > 0:
                    str_ = str_[:-1]
            else:
                str_ += s[i]

        return str_


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            bs = 0
            while i >= 0:
                if s[i] == '#':
                    bs += 1
                    i -= 1
                elif bs > 0:
                    bs -= 1
                    i -= 1
                else:
                    break

            bs = 0
            while j >= 0:
                if t[j] == '#':
                    bs += 1
                    j -= 1
                elif bs > 0:
                    bs -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            if (i < 0 <= j) or (i >= 0 > j):
                return False

            i -= 1
            j -= 1

        return True