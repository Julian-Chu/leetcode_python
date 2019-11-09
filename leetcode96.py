from unittest import TestCase


class Solution:
    def numTrees(self, n: int) -> int:
        if n==0:
            return 1
        if n==1 or n==2:
            return n
        if n==3:
            return 5
        sum=0
        for i in range(1,n//2+1):
            sum+= self.numTrees(i-1)*self.numTrees(n-i)
        sum*=2
        if n%2==1:
            temp = self.numTrees(n//2)
            sum+=temp*temp
        return sum


class TestSolution(TestCase):
    def test_numTrees(self):
        test_cases = [
            {
                "name": "3",
                "input": 3,
                "expected": 5
            },
            {
                "name": "4",
                "input": 4,
                "expected": 14
            },
        ]

        solution = Solution()
        for ts in test_cases:
            self.assertEqual(ts["expected"], solution.numTrees(ts["input"]))
