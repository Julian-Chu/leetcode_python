class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, chars):
        l, r = 0, len(chars) - 1

        while l <= r:
            while l <= r and chars[l] >= 'a':
                l += 1
            while l <= r and chars[r] < 'a':
                r -= 1
            if l <= r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1

