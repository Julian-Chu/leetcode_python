class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        return self.is_match_helper(s, 0, p, 0, {})

    def is_match_helper(self, s, s_index, p, p_index, memo):
        key = (s_index, p_index)
        if key in memo:
            return memo[key]

        if len(p) == p_index:
            return len(s) == s_index

        if len(s) == s_index:
            return self.is_empty(p[p_index:])

        match = False
        if p_index + 1 < len(p) and p[p_index + 1] == '*':
            match = self.is_char_match(s[s_index], p[p_index]) and self.is_match_helper(s, s_index + 1, p, p_index,
                                                                                        memo) or self.is_match_helper(s,
                                                                                                                      s_index,
                                                                                                                      p,
                                                                                                                      p_index + 2,
                                                                                                                      memo)
        else:
            match = self.is_char_match(s[s_index], p[p_index]) and self.is_match_helper(s, s_index + 1, p, p_index + 1,
                                                                                        memo)

        memo[key] = match
        return match

    def is_char_match(self, s, p):
        return s == p or p == '.'

    def is_empty(self, p):
        if len(p) % 2 == 1:
            return False

        for i in range(1, len(p), 2):
            if p[i] != '*':
                return False

        return True


class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[len(s)][len(p)]