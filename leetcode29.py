from unittest import TestCase


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 0:
            return 0

        res = self.divideAbs(abs(dividend), abs(divisor))
        if (dividend > 0 > divisor) or (dividend < 0 < divisor):
            res = -res

        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648

        return res

    def divideAbs(self, dividend, divisor) -> int:
        if dividend < divisor:
            return 0
        temp = divisor
        cnt = 1
        while dividend > temp << 1:
            temp = temp << 1
            cnt = cnt << 1

        return cnt + self.divideAbs(dividend - temp, divisor)


class TestSolution(TestCase):
    def test_divide(self):
        test_cases = [
            {
                "name": "10/3",
                "dividend": 10,
                "divisor": 3,
                "expected": 3
            },
            {
                "name": "7/-3",
                "dividend": 7,
                "divisor": -3,
                "expected": -2
            },
            {
                "name": "-1/1",
                "dividend": -1,
                "divisor": 1,
                "expected": -1
            },

            {
                "name": "1/1",
                "dividend": 1,
                "divisor": 1,
                "expected": 1
            },

            {
                "name": "-2147483648/-1",
                "dividend": -2147483648,
                "divisor": -1,
                "expected": 2147483647
            },

            {
                "name": "-2147483648/1",
                "dividend": -2147483648,
                "divisor": 1,
                "expected": -2147483648
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.divide(testcase["dividend"], testcase["divisor"]),
                             testcase["name"])
