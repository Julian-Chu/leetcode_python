"""
set, can use array as well
"""
class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        visited = set()
        nums = self.dfs(str, visited, n)
        # print(visited)
        for i in range(1, n + 1):
            if i not in visited:
                return i
        return 0

    def dfs(self, string, visited, n):
        # if len(visited) > 15:
        #     print(visited)
        #     print(string)
        # print(str)
        if string == "":
            return True

        for i in range(2):
            num = int(string[:i + 1])
            # print(num)
            if num == 0 or num > n:
                break
            if num not in visited:
                visited.add(num)
                if self.dfs(string[i + 1:], visited, n):
                    return True
                visited.remove(num)
        return False