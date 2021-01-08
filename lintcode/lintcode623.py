


"""
memo
"""
class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """

    def kDistance(self, words, target, k):
        result = []
        memo = {}
        for word in words:
            step = self.dfs(word, target, memo)
            if step <= k:
                result.append(word)
        return result

    def dfs(self, word, target, memo):
        if word == target:
            return 0
        if not word:
            return len(target)
        if not target:
            return len(word)
        key = (word, target)
        if key in memo:
            return memo[key]

        if word[0] == target[0]:
            memo[key] = self.dfs(word[1:], target[1:], memo)
            return memo[key]

        res = min(
            self.dfs(word[1:], target, memo),
            self.dfs(word, target[1:], memo),
            self.dfs(word[1:], target[1:], memo)
        ) + 1

        memo[key] = res
        return res