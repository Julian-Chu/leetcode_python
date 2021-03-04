class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        result = []
        self.dfs(n, 2, [], result)
        return result

    def dfs(self, n, start_factor, combination, combinations):
        if len(combination) > 0:
            combinations.append(combination[:] + [n])

        for i in range(start_factor, int(math.sqrt(n)) + 1):
            if n % i == 0:
                combination.append(i)
                self.dfs(n // i, i, combination, combinations)
                combination.pop()


class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        return self.dfs(n, {})

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]

        partitions = []
        bound = int(n ** 0.5)
        for i in range(2, bound + 1):
            if n % i == 0:
                partitions.append([i, n // i])
                subs = self.dfs(n // i, memo)
                for sub in subs:
                    if i > sub[0]:
                        continue
                    partitions.append([i] + sub)
        memo[n] = partitions
        return partitions

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        result = []
        self.helper(result, [], n, 2)
        return result

    def helper(self, result, item, n, start):
        if n <= 1:
            if len(item) > 1:
                result.append(item[:])
            return

        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                item.append(i)
                self.helper(result, item, n // i, i)
                item.pop()
        # only factor 1 and n remained
        if n >= start:
            item.append(n)
            self.helper(result, item, 1, n)
            item.pop()