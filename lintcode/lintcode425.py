class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    numberToLetters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def letterCombinations(self, digits):
        if not digits:
            return []
        results = []
        self.dfs(digits, 0, [], results)
        return results

    def dfs(self, digits, index, chars, results):
        if len(chars) == len(digits):
            results.append(''.join(chars))
            return

        number = digits[index]
        for letter in self.numberToLetters[number]:
            chars.append(letter)
            self.dfs(digits, index + 1, chars, results)
            chars.pop()