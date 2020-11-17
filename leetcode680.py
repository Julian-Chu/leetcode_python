class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1

        if left >= right:
            return True

        return self.isPalidrome(s, left + 1, right) or self.isPalidrome(s, left, right - 1)

    def isPalidrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution1:
    def validPalindrome(self, s: str) -> bool:
        if s is None:
            return False

        left, right = self.findDiff(s, 0, len(s) - 1)
        if left >= right:
            return True

        return self.isPalidrome(s, left + 1, right) or self.isPalidrome(s, left, right - 1)

    def isPalidrome(self, s, left, right):
        left, right = self.findDiff(s, left, right)
        return left >= right

    def findDiff(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1

        return left, right
