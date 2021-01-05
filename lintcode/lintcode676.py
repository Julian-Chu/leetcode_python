class Solution:
    def __init__(self):
        self.decodeDict = {}

    """
    @param s: a message being encoded
    @return: an integer
    """

    def numDecodings(self, s):
        if not s:
            return 0
        mod = 10 ** 9 + 7
        n = len(s)
        n2 = 1
        n1 = self.decode(s[0])
        n0 = n1
        for i in range(2, n + 1):
            n0 = (n1 * self.decode(s[i - 1:i]) % mod + n2 * self.decode(s[i - 2:i]) % mod) % mod
            n1, n2 = n0, n1

        return n0

    def decode(self, s):
        decodeDict = self.decodeDict
        key = s
        if key in decodeDict:
            return decodeDict[key]

        if len(s) == 0:
            decodeDict[key] = 1
            return 1

        if len(s) == 1:
            if s == '*':
                decodeDict[key] = 9
                return 9
            if 0 < int(s) <= 9:
                decodeDict[key] = 1
                return 1
            decodeDict[key] = 0
            return 0

        if len(s) == 2:
            if s == "**":
                decodeDict[key] = 15
                return 15  # 11-19,  21-26
            if s[0] == '*':  # 1 or 2
                num = int(s[1])
                if 1 <= num <= 6:
                    decodeDict[key] = 2
                    return 2
                elif 7 <= num <= 9:
                    decodeDict[key] = 1
                    return 1
                return 0
            if s[1] == '*':
                if s[0] == '1':
                    decodeDict[key] = 9
                    return 9  # 11-19
                if s[0] == '2':
                    decodeDict[key] = 2
                    return 6  # 21-26
                return 0
            if 10 <= int(s) <= 26:
                decodeDict[key] = 1
                return 1
        decodeDict[key] = 0
        return 0


class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """

    def numDecodings(self, s):
        if not s:
            return 0
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [0] * (3)
        dp[0] = 1
        dp[1] = self.decode(s[0])

        for i in range(2, n + 1):
            dp[i % 3] = (dp[(i - 1) % 3] * self.decode(s[i - 1:i]) % mod +
                         dp[(i - 2) % 3] * self.decode(s[i - 2:i]) % mod) % mod

        return dp[n % 3]

    def decode(self, s):
        if len(s) == 0:
            return 1

        if len(s) == 1:
            if s == '*':
                return 9
            if 0 < int(s) <= 9:
                return 1
            return 0

        if len(s) == 2:
            if s == "**":
                return 15  # 11-19,  21-26
            if s[0] == '*':  # 1 or 2
                num = int(s[1])
                if 1 <= num <= 6:
                    return 2
                elif 7 <= num <= 9:
                    return 1
                return 0
            if s[1] == '*':
                if s[0] == '1':
                    return 9  # 11-19
                if s[0] == '2':
                    return 6  # 21-26
                return 0
            if 10 <= int(s) <= 26:
                return 1
        return 0


class Solution:
    """
    @param s: a message being encoded
    @return: an integer
    """

    def numDecodings(self, s):
        if not s:
            return 0
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = self.decode(s[0])

        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] * self.decode(s[i - 1:i]) % mod +
                     dp[i - 2] * self.decode(s[i - 2:i]) % mod) % mod

        return dp[-1]

    def decode(self, s):
        if len(s) == 0:
            return 1

        if len(s) == 1:
            if s == '*':
                return 9
            if 0 < int(s) <= 9:
                return 1
            return 0

        if len(s) == 2:
            if s == "**":
                return 15  # 11-19,  21-26
            if s[0] == '*':  # 1 or 2
                num = int(s[1])
                if 1 <= num <= 6:
                    return 2
                elif 7 <= num <= 9:
                    return 1
                return 0
            if s[1] == '*':
                if s[0] == '1':
                    return 9  # 11-19
                if s[0] == '2':
                    return 6  # 21-26
                return 0
            if 10 <= int(s) <= 26:
                return 1
        return 0





