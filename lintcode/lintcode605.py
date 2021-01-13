class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org

    def build_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def get_indegres(self, graph):
        indegrees = {
            node: 0 for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees

    def topological_sort(self, graph):
        indegrees = self.get_indegres(graph)

        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)

        topo_order = []
        while queue:
            if len(queue) > 1:
                return None

            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        if len(topo_order) == len(graph):
            return topo_order
        return None


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        graph = {num: [] for num in org}
        indegree = {num: 0 for num in org}
        nums_in_seqs = {num: False for num in org}
        for seq in seqs:
            for i in range(0, len(seq)):
                if seq[i] not in graph:
                    return False
                if i == 0:
                    nums_in_seqs[seq[0]] = True
                else:
                    node_out = seq[i - 1]
                    node_in = seq[i]
                    graph[node_out].append(node_in)
                    indegree[node_in] += 1
                    nums_in_seqs[node_in] = True
                    nums_in_seqs[node_out] = True

        for key in nums_in_seqs:
            if nums_in_seqs[key] == False:
                return False

        queue = collections.deque()
        for num in indegree:
            if indegree[num] == 0:
                queue.append(num)

        sequence = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            sequence.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        return sequence == org
