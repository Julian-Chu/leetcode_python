class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        visited = set()
        queue = collections.deque([node])

        while queue:
            node = queue.popleft()
            if values[node] == target:
                return node
            visited.add(node)
            for next_node in node.neighbors:
                if next_node in visited:
                    continue
                queue.append(next_node)
        return None