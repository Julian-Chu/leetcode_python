class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.isValid(s[left]):
                left += 1
            while left < right and not self.isValid(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def isValid(self, character):
        return character.isdigit() or character.isalpha()


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True

        a = ""
        for character in s:
            if character.isalnum():
                a = a + character
        return a[::-1].lower() == a.lower()


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''.join(ch for ch in s if ch.isalnum()).lower()
        return newStr == newStr[::-1]
