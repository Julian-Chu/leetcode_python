from unittest import TestCase


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2 == '0':
            return "0"
        temp = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp[i + j + 1] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

        temp = temp[::-1]
        for i in range(len(temp)):
            if temp[i] >= 10:
                temp[i + 1] += temp[i] // 10
                temp[i] = temp[i] % 10

        temp = temp[::-1]
        if temp[0] == 0:
            temp = temp[1:]
        temp = [v + ord('0') for v in temp]
        return bytes(temp).decode()


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
