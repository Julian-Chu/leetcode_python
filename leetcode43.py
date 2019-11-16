from unittest import TestCase


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        val1 = 0
        val2 = 0
        m1 = 1
        m2 = 1

        for l1 in num1[::-1]:
            val1 += values.index(l1) * m1
            m1 *= 10

        for l2 in num2[::-1]:
            val2 += values.index(l2) * m2
            m2 *= 10

        prod = val1 * val2

        res = ""
        while prod != 0:
            res = values[prod % 10] + res
            prod //= 10

        if res == "":
            res = "0"
        return res


class TestSolution(TestCase):
    def test_multiply(self):
        test_cases = [
            {
                "name": "2*3",
                "num1": "2",
                "num2": "3",
                "expected": "6"
            },
            {
                "name": "123*456",
                "num1": "123",
                "num2": "456",
                "expected": "56088"
            },
            {
                "name": "900*900",
                "num1": "900",
                "num2": "900",
                "expected": "810000"
            },
            {
                "name": "9133*0",
                "num1": "9133",
                "num2": "0",
                "expected": "0"
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.multiply(testcase["num1"], testcase["num2"]),
                             testcase["name"])
