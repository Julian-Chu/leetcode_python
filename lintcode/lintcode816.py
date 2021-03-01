class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        graph = self.construct_graph(roads, n)
        state_size = 1 << n
        f = [
            [float('inf')] * (n + 1)
            for _ in range(state_size)
        ]   # f[x][y]  x: state,  y: destination which from previous state goes to
        f[1][1] = 0
        for state in range(state_size):
            for i in range(2, n + 1): # 1確定走過
                if state & (1 << (i - 1)) == 0:
                    continue
                prev_state = state ^ (1 << (i - 1))
                for j in range(1, n + 1):  # 前一個狀態有可能是由1開始,  enumerate all possible previous destination
                    if prev_state & (1 << (j - 1)) == 0:
                        continue
                    f[state][i] = min(f[state][i], f[prev_state][j] + graph[j][i])
        return min(f[state_size - 1])

    def construct_graph(self, roads, n):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        return graph


class Result:
    def __init__(self):
        self.min_cost = float('inf')


class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        graph = self.construct_graph(roads, n)
        result = Result()
        self.dfs(1, n, [1], set([1]), 0, graph, result)
        return result.min_cost

    def dfs(self, city, n, path, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return

        for next_city in graph[city]:
            if next_city in visited:
                continue
            if self.has_better_path(graph, path, next_city):
                continue
            visited.add(next_city)
            path.append(next_city)
            self.dfs(
                next_city,
                n,
                path,
                visited,
                cost + graph[city][next_city],
                graph,
                result)
            path.pop()
            visited.remove(next_city)

    def construct_graph(self, roads, n):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        return graph

    def has_better_path(self, graph, path, city):
        for i in range(1, len(path)):
            if graph[path[i - 1]][path[i]] + graph[path[-1]][city] > \
                    graph[path[i - 1]][path[-1]] + graph[path[i]][city]:
                return True
        return False


class Result:
    def __init__(self):
        self.min_cost = float('inf')


class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        graph = self.construct_graph(roads, n)
        result = Result()
        self.dfs(1, n, set([1]), 0, graph, result)
        return result.min_cost

    def dfs(self, city, n, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return

        for next_city in graph[city]:
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(next_city, n, visited, cost + graph[city][next_city], graph, result)
            visited.remove(next_city)

    def construct_graph(self, roads, n):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, c in roads:
            graph[a][b] = min(graph[a][b], c)
            graph[b][a] = min(graph[b][a], c)
        return graph


class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        if n == 1:
            return 0
        visited = set()
        self.result = float('inf')
        roadsmap = {num + 1: [] for num in range(n)}
        for road in roads:
            roadsmap[road[0]].append((road[1], road[2]))
            roadsmap[road[1]].append((road[0], road[2]))
        visited.add(1)
        print(roadsmap)
        self.dfs(n, 1, roadsmap, 0, visited)
        return self.result

    def dfs(self, n, start, roadsmap, cost, visited):
        if len(visited) == n:
            self.result = min(cost, self.result)
            return

        for road in roadsmap[start]:
            to = road[0]
            if to in visited:
                continue
            visited.add(to)
            self.dfs(n, to, roadsmap, cost + road[1], visited)
            visited.remove(to)