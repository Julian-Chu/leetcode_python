from unittest import TestCase


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1s = version1.split(".")
        v2s = version2.split(".")
        v1int = []
        v2int = []

        for s in v1s:
            v1int.append(int(s))

        for s in v2s:
            v2int.append(int(s))

        i = len(v1int) - 1
        while i >= 0:
            if v1int[i] != 0:
                break
            v1int = v1int[:i]
            i -= 1

        i = len(v2int) - 1
        while i >= 0:
            if v2int[i] != 0:
                break
            v2int = v2int[:i]
            i -= 1

        l = len(v1int)
        if l > len(v2int):
            l = len(v2int)

        for i in range(l):
            if v1int[i] > v2int[i]:
                return 1
            if v1int[i] < v2int[i]:
                return -1

        if len(v1int)>len(v2int):
            return 1
        if len(v1int)<len(v2int):
            return -1
        return 0


class TestSolution(TestCase):
    def test_compareVersion(self):
        test_cases = [
            {
                "name": "0.1 vs 1.1",
                "version1": "0.1",
                "version2": "1.1",
                "expected": -1
            },
            {
                "name": "1.0.1 vs 1",
                "version1": "1.0.1",
                "version2": "1",
                "expected": 1
            },
            {
                "name": "7.5.2.4 vs 7.5.3",
                "version1": "7.5.2.4",
                "version2": "7.5.3",
                "expected": -1
            },
            {
                "name": "1.01 vs 1.001",
                "version1": "1.01",
                "version2": "1.001",
                "expected": 0
            },
            {
                "name": "1.0 vs 1.0.0",
                "version1": "1.0",
                "version2": "1.0.0",
                "expected": 0
            }
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.compareVersion(testcase["version1"], testcase["version2"]),
                             testcase["name"])
