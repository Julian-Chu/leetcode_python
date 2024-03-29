from unittest import TestCase


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        x, y = 1, 1

        for i in range(2, n+1):
            x, y = x + y, x
        return x


class TestSolution(TestCase):
    def test_climbStairs(self):
        test_cases = [
            {
                "name": "2",
                "input": 2,
                "expected": 2
            },
            {
                "name": "3",
                "input": 3,
                "expected": 3
            },
            {
                "name": "4",
                "input": 4,
                "expected": 5
            },

        ]

        solution = Solution();
        for ts in test_cases:
            self.assertEqual(solution.climbStairs(ts["input"]), ts["expected"])


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        steps = [0] * (n+1)

        steps[0] = 1
        steps[1] = 1

        for i in range(2, n+1):
            steps[i] = steps[i-1] + steps[i-2]

        return steps[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        steps = [0] * (2)

        steps[0] = 1
        steps[1] = 1

        for i in range(2, n+1):
            steps[i%2] = steps[(i-1)%2] + steps[(i-2)%2]

        return steps[n%2]