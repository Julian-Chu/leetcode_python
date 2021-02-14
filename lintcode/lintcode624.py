class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    import collections
    def minLength(self, s, dict):
        if not s:
            return 0
        if len(dict) == 0:
            return len(s)

        visited = set()

        queue = collections.deque([s])
        # 不能用string 當最後輸出結果
        # 最後一輪queue 可能有兩個以上的string
        min_len = float('inf')
        while queue:
            for _ in range(len(queue)):
                string = queue.popleft()
                min_len = min(min_len, len(string))
                for substr in dict:
                    pos = string.find(substr)
                    while pos != -1:
                        if string == substr:
                            return 0
                        str_removed = string[:pos] + string[pos + len(substr):]
                        if str_removed in visited:
                            break
                        visited.add(str_removed)
                        # import: 不能用pos+key長度 成為下一個開始的位置  ex: aaaa find aa
                        pos = string.find(substr, pos + 1)
                        queue.append(str_removed)

        return min_len


"""
bad performance
"""
import collections
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    import collections
    def minLength(self, s, dict):
        if not s:
            return 0
        if len(dict) == 0:
            return len(s)

        visited = set()

        queue = collections.deque([s])
        min_len = float('inf')
        while queue:
            for _ in range(len(queue)):
                string = queue.popleft()
                if string in visited:
                    continue
                visited.add(string)
                min_len = min(min_len, len(string))
                for substr in dict:
                    if substr not in string:
                        continue
                    for i in range(len(string)):
                        if string[i:i + len(substr)] == substr:
                            remove_substr = string[0:i] + string[i + len(substr):]
                            if remove_substr == "":
                                return 0
                            queue.append(remove_substr)
        return min_len

