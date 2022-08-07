class Solution:
    def __init__(self):
        self.dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.res = []
        self.tmp = ""

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.dfs(digits, 0)
        return self.res

    def dfs(self, digits, index):
        if index == len(digits):
            self.res.append(self.tmp)
            return
        num = digits[index]

        for letter in self.dic[num]:
            self.tmp += letter
            self.dfs(digits, index + 1)
            self.tmp = self.tmp[:-1]