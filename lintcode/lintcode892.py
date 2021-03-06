from heapq import heapify, heappop, heappush


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        graph = self.build_graph(words)
        if not graph:
            return ""
        return self.topological_sort(graph)

    def build_graph(self, words):
        graph = {}

        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        n = len(words)
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                # the dictionary is invalid, if a is prefix of b and b is appear before a
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(
                            words[i + 1]):  # words[i] is longer than words[i+1], but words[i+1] is prefix for words[i]
                        return None
        return graph

    def topological_sort(self, graph):
        indegree = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        # use headq instead of regular queue so that we can get the smallest lexicographical order
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)

        # regular bfs algorithm to do topological sorting
        topo_order = ""
        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)

        # if all nodes popped
        if len(topo_order) == len(graph):
            return topo_order

        return ""


from heapq import *


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Construct Graph
        in_degree = {ch: 0 for word in words for ch in word}
        neighbors = {ch: [] for word in words for ch in word}
        for pos in range(len(words) - 1):
            for i in range(min(len(words[pos]), len(words[pos + 1]))):
                pre, next = words[pos][i], words[pos + 1][i]
                if pre != next:
                    in_degree[next] += 1
                    neighbors[pre].append(next)
                    break
                if i == min(len(words[pos]), len(words[pos + 1])) - 1:
                    if len(words[pos]) > len(words[pos + 1]):
                        return ""

        # Topological Sort
        heap = [ch for ch in in_degree if in_degree[ch] == 0]
        heapify(heap)
        order = []
        while heap:
            for _ in range(len(heap)):
                ch = heappop(heap)
                order.append(ch)
                for child in neighbors[ch]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        heappush(heap, child)

        # order is invalid
        if len(order) != len(in_degree):
            return ""
        return ''.join(order)