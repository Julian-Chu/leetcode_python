class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if target == "":
            return 0
        if source == "":
            return -1

        target_size = len(target)
        source_size = len(source)

        for i in range(source_size - target_size):
            if source[i:i+target_size] == target:
                return i
        return -1


class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        if target == "":
            return 0
        if source == "":
            return -1

        len_t = len(target)
        len_s = len(source)

        for i in range(len_s - len_t + 1):
            j = 0
            while j < len_t:
                if source[i+j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1

