class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):

        # n nodes , n-1 edges => tree or not connected graph with circle
        if len(edges) != n - 1:
            return False

        neighbors = {num: [] for num in range(n)}
        for u, v in edges:
            if u not in neighbors:
                neighbors[u] = []
            if v not in neighbors:
                neighbors[v] = []
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {}
        queue = collections.deque()
        queue.append(0)
        visited[0] = True
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True
                    queue.append(node)
        return len(visited) == n