from unittest import TestCase


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_byte = [(ord(x) - ord('0')) for x in a]
        b_byte = [(ord(x) - ord('0')) for x in b]

        res = ""

        idx1 = len(a) - 1
        idx2 = len(b) - 1

        previous = 0
        while idx1 >= 0 or idx2 >= 0:
            v1 = 0
            v2 = 0
            if idx1 >= 0:
                v1 = a_byte[idx1]
                idx1 -= 1
            if idx2 >= 0:
                v2 = b_byte[idx2]
                idx2 -= 1
            res = str((v1 + v2 + previous) % 2) + res
            previous = (v1 + v2 + previous) // 2

        if previous != 0:
            res = str(previous)+res
        return res


class TestSolution(TestCase):
    def test_addBinary(self):
        test_cases = [
            {
                "name": "11 + 1",
                "a": "11",
                "b": "1",
                "expected": "100"
            },
            {
                "name": "1010 1011",
                "a": "1010",
                "b": "1011",
                "expected": "10101"
            }
        ]

        solution = Solution();
        for ts in test_cases:
            self.assertEqual(solution.addBinary(ts["a"], ts["b"]), ts["expected"])
