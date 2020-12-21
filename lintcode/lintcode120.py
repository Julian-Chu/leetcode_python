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

"""
two way bfs
"""
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    import collections
    def ladderLength(self, start, end, dict):

        dict.add(start)
        dict.add(end)
        graph = self.construct_graph(dict)
        print(graph)
        forward_queue = collections.deque([start])
        forward_set = set([start])
        backward_queue = collections.deque([end])
        backward_set = set([end])

        distance = 1
        while forward_queue and backward_queue:
            distance += 1
            if self.extend_queue(graph, forward_queue, forward_set, backward_set):
                return distance
            distance += 1
            if self.extend_queue(graph, backward_queue, backward_set, forward_set):
                return distance
        return distance

    def extend_queue(self, graph, queue, visited, opposite_visited):
        for _ in range(len(queue)):
            word = queue.popleft()
            for next_word in graph[word]:
                if next_word in visited:
                    continue
                if next_word in opposite_visited:
                    return True
                queue.append(next_word)
                visited.add(next_word)
        return False

    def construct_graph(self, word_set):
        graph = {}
        for word in word_set:
            graph[word] = self.get_next_words(word, word_set)
        return graph

    def get_next_words(self, word, word_set):
        chars = "abcdefghijklmnopqrstuvwxyz"
        next_words = set()
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i + 1:]
            for ch in chars:
                if word[i] == ch:
                    continue
                next_word = prefix + ch + suffix
                if next_word in word_set:
                    next_words.add(next_word)
        return next_words

