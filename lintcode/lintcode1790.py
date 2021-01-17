class Solution:
    """
    @param str: A String
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        offset = (left - right) % len(str)
        if offset < 0:
            offset = len(str) + offset
        str =  str[offset:] +  str[0:offset]
        return str