"""
manacher
"""
class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return ""
        # Using manacher's algorithm
        # abba => #a#b#b#a#
        chars = []
        for c in s:
            chars.append('#')
            chars.append(c)
        chars.append('#')

        n = len(chars)
        palindrome = [0] * n
        palindrome[0] = 1

        # mid: center for longest palindromic string
        # longest: length of lonest palindromic string
        mid, longest = 0, 1
        for i in range(1, n):
            length = 1
            if mid + longest > i:
                # j = 2 * id - i，也就是说 j 是 i 关于 id 的对称点(j = id - (i - id))
                # if (mx - i > P[j])
                #     P[i] = P[j];
                # else /* P[j] >= mx - i */
                #     P[i] = m
                mirror = mid - (i - mid)
                length = min(palindrome[mirror], mid + longest - i)

            while i + length < len(chars) and i - length >= 0:
                if chars[i + length] != chars[i - length]:
                    break
                length += 1

            if length > longest:
                longest = length
                mid = i
            palindrome[i] = length

        longest = longest - 1
        start = (mid - 1) // 2 - (longest - 1) // 2
        return s[start:start + longest]


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return ""
        size = len(s)
        maxLen = 1
        subStrIndex = 0

        for mid in range(size):
            left = mid
            right = mid
            while left - 1 >= 0 and s[mid] == s[mid - 1]:
                left -= 1
            while right + 1 < size and s[mid] == s[mid + 1]:
                right += 1

            while left >= 0 and right < size:
                if s[left] != s[right]:
                    break
                substrLen = right - left + 1
                if substrLen > maxLen:
                    maxLen = substrLen
                    subStrIndex = left

                right += 1
                left -= 1

        return s[subStrIndex:subStrIndex + maxLen]


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return ""
        size = len(s)
        longestStr = ""

        for mid in range(size):
            subStr = self.findPalindrome_from(s, mid, mid)
            if len(subStr) > len(longestStr):
                longestStr = subStr
            subStr = self.findPalindrome_from(s, mid, mid + 1)
            if len(subStr) > len(longestStr):
                longestStr = subStr

        return longestStr

    def findPalindrome_from(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            right += 1
            left -= 1
        return s[left + 1:right]


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)
        is_palindrome = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True

        longest, start, end = 1, 0, 0
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                is_palindrome[i][j] = (s[i] == s[j] and (is_palindrome[i + 1][j - 1] or i + 1 >= j - 1))

                if is_palindrome[i][j] and length + 1 > longest:
                    longest = length + 1
                    start, end = i, j

        return s[start:end + 1]
