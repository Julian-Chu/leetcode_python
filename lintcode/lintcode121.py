class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        res = []
        dict.add(end)
        layer = {}
        # key is the last word
        layer[start] = [[start]]

        while layer:
            print(layer)
            newlayer = collections.defaultdict(list)
            for word in layer:
                if word == end:
                    res.extend(k for k in layer[word])
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in dict:
                                newlayer[new_word] += [j + [new_word] for j in layer[word]]
            dict -= set(newlayer.keys())
            layer = newlayer
        return res


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        indexes = self.build_indexes(dict)
        distance = self.bfs(end, indexes)
        results = []
        self.dfs(start, end, distance, indexes, [start], results)
        return results

    def build_indexes(self, dict):
        indexes = {}
        for word in dict:
            for i in range(len(word)):
                key = word[:i] + '%' + word[i + 1:]
                if key in indexes:
                    indexes[key].add(word)
                else:
                    indexes[key] = set([word])
        return indexes

    # get all distance to end
    def bfs(self, end, indexes):
        distance = {end: 0}
        queue = collections.deque([end])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, indexes):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
        return distance

    def get_next_words(self, word, indexes):
        words = []
        for i in range(len(word)):
            key = word[:i] + '%' + word[i + 1:]
            for w in indexes.get(key, []):
                words.append(w)
        return words

    def dfs(self, curt, target, distance, indexes, path, results):
        if curt == target:
            results.append(list(path))
            return

        for word in self.get_next_words(curt, indexes):
            # find the next shortest path
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, indexes, path, results)
            path.pop()