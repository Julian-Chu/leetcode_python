import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        used = {start, end}
        queue = collections.deque([start])
        result = 0
        while queue:
            result += 1
            # print(queue)
            # print(result)
            for _ in range(len(queue)):
                word = queue.popleft()

                if self.checkDiff(word, end) == 1:
                    # print(word, end)
                    return result + 1

                for i in range(len(word)):
                    next_word = word
                    for ch in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                        next_word = next_word[:i] + ch + next_word[i + 1:]
                        if next_word == word:
                            continue
                        if next_word in dict and next_word not in used:
                            used.add(next_word)
                            queue.append(next_word)

        return 0

    def checkDiff(self, str1, str2):
        diff = 0

        size = len(str1)
        for i in range(size):
            if str1[i] != str2[i]:
                diff += 1

        return diff


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        visited = {start}
        queue = collections.deque([start])
        result = 0
        while queue:
            result += 1
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == end:
                    return result

                for i in range(len(word)):
                    next_word = word
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = next_word[:i] + ch + next_word[i + 1:]
                        if next_word == word:
                            continue
                        if next_word in dict and next_word not in visited:
                            visited.add(next_word)
                            queue.append(next_word)

        return 0
