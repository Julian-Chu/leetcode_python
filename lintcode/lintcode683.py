class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if not s:
            return 0

        ans = 0
        lowercase_dic = set()
        for key in dict:
            lowercase_dic.add(key.lower())

        memo = {}
        for end in range(0, len(s)):
            ans += self.cutWord(0, end, s.lower(), lowercase_dic, memo)

        return ans

    def cutWord(self, start, end, s, dict, memo):

        if (start, end) in memo:
            return memo[(start, end)]

        word = s[start:end + 1]
        if word not in dict:
            return 0

        if end + 1 == len(s):
            return 1

        cnt = 0
        for i in range(end + 1, len(s)):
            cnt += self.cutWord(end + 1, i, s, dict, memo)

        memo[(start, end)] = cnt

        return cnt


class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0

        max_length, lower_dict = self.initialize(dict)
        return self.memo_search(s.lower(), 0, max_length, lower_dict, {})

    def memo_search(self, s, index, max_length, lower_dict, memo):
        if index == len(s):
            return 1

        if index in memo:
            return memo[index]

        memo[index] = 0
        for i in range(index, len(s)):
            if i + 1 - index > max_length:
                break
            word = s[index: i + 1]
            if word not in lower_dict:
                continue
            memo[index] += self.memo_search(s, i + 1, max_length, lower_dict, memo)
        return memo[index]

    def initialize(self, dict):
        max_length = 0
        lower_dict = set()
        for word in dict:
            max_length = max(max_length, len(word))
            lower_dict.add(word.lower())
        return max_length, lower_dict


class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0

        lower_dict = set()
        max_length = 0
        for word in dict:
            lower_dict.add(word.lower())
            max_length = max(max_length, len(word))
        s = s.lower()
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string

        for i in range(n):
            for j in range(i, n):
                if s[i:j + 1] in lower_dict:
                    dp[j + 1] += dp[i]

        return dp[n]