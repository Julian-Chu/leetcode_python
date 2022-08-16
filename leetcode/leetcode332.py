class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[1])
        used = [0] * len(tickets)
        res = ["JFK"]

        def dfs():
            if sum(used) == len(tickets):
                return True

            for i in range(len(tickets)):
                if used[i] == 1:
                    continue

                start, end = tickets[i]
                if start != res[-1]:
                    continue

                used[i] = 1
                res.append(end)
                if dfs():
                    return True
                res.pop()
                used[i] = 0

        dfs()

        return res