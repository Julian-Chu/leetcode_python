class Solution: # prunning
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []

        results = []
        memo = {}
        max_length = self.get_max_length(wordDict)
        self.dfs(s, 0, max_length, wordDict, {}, [], results)
        return results

    def dfs(self, s, index, max_length, wordDict, memo, result, results):
        if index == len(s):
            results.append(" ".join(result))
            return

        if not self.is_possible(s, index, max_length, wordDict, memo):
            return

        for i in range(index, len(s)):
            if i + 1 - index > max_length:
                break
            word = s[index:i + 1]
            if word not in wordDict:
                continue
            result.append(word)
            self.dfs(s, i + 1, max_length, wordDict, memo, result, results)
            result.pop()

    def is_possible(self, s, index, max_length, word_set, memo):
        if index in memo:
            return memo[index]
        if index == len(s):
            memo[index] = True
            return True

        memo[index] = False

        for i in range(index, len(s)):
            if i + 1 - index > max_length:
                break
            word = s[index:i + 1]
            if word not in word_set:
                continue
            if self.is_possible(s, i + 1, max_length, word_set, memo):
                memo[index] = True
                break
        return memo[index]

    def get_max_length(self, word_set):
        max_length = 0
        for word in word_set:
            max_length = max(max_length, len(word))
        return max_length