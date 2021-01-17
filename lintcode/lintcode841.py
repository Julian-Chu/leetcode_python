"""
Rabin-Karp
"""
class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """

    def stringReplace(self, a, b, s):
        # hase base
        seed = 31
        # mod
        mod = 10000007
        # string hash in of a
        aHash = []
        # prefix hash of s
        sHash = []
        base = []
        for i in a:
            tmp = 0
            for j in i:
                tmp = tmp * seed + (ord(j) - ord('a'))
                tmp = tmp % mod
            aHash.append(tmp)

        sTmp = 0
        baseTmp = 1
        base.append(baseTmp)
        sHash.append(sTmp)
        for i in s:
            sTmp = sTmp * seed + (ord(i) - ord('a'))
            sTmp = sTmp % mod
            sHash.append(sTmp)
            baseTmp = (baseTmp * seed) % mod
            base.append(baseTmp)

        ans = ""
        i = 0
        slen = len(s)
        while i < slen:
            max_aLen = 0
            idx = -1
            for j in range(len(a)):
                aLen = len(a[j])
                if i + aLen > slen:
                    continue
                A = aHash[j]
                S = (sHash[i + aLen] - base[aLen] * sHash[i]) % mod  # hash of s substring
                A = A % mod
                S = (S + mod) % mod  # avoid S < 0
                if A == S and max_aLen < aLen:
                    max_aLen = aLen
                    idx = j
            if idx == -1:
                ans = ans + s[i:i + 1]
                i = i + 1
            else:
                ans = ans + b[idx]
                i = i + max_aLen
        return ans

"""
normal way
"""
class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """

    def stringReplace(self, a, b, s):
        hashmap = {}

        lengths = set()
        for i in range(len(a)):
            hashmap[a[i]] = b[i]
            lengths.add(len(a[i]))

        lengths = list(lengths)
        lengths.sort(reverse=True)

        result = ""
        start = 0

        while start < len(s):
            found = False
            for l in lengths:
                end = start + l
                if end > len(s):
                    continue

                str = s[start:end]
                if str in a:
                    result += hashmap[str]
                    found = True
                    start = end
                    break

            if not found:
                result += s[start]
                start += 1

        return result

