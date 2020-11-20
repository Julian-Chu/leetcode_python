class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        letterCount = {}

        singleChars = 0
        for letter in s:
            if letter not in letterCount:
                letterCount[letter] = 1
            else:
                letterCount[letter] += 1

            if letterCount[letter] & 1 == 1:
                singleChars += 1
            else:
                singleChars -= 1

        if singleChars > 0:
            return len(s) - singleChars + 1
        return len(s)



