class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        return self.dfs(s, p, 0, 0, {})

    def dfs(self, s, p, s_index, p_index, memo):
        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]
        if p_index >= len(p):
            return s_index >= len(s)

        if s_index >= len(s):
            for i in range(p_index, len(p)):
                if p[i] != "*":
                    return False
            return True

        match = False
        if p[p_index] == "*":
            for i in range(s_index, len(s) + 1):
                if self.dfs(s, p, i, p_index + 1, memo):
                    match = True
                    break

        if p[p_index] == "?" or s[s_index] == p[p_index]:
            match = self.dfs(s, p, s_index + 1, p_index + 1, memo)

        memo[(s_index, p_index)] = match
        return match

