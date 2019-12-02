from unittest import TestCase


class Solution:
    def simplifyPath(self, path: str) -> str:
        splitStr = path.split("/")
        moveUpCount = 0
        res = ''

        for p in reversed(splitStr):
            if p == '.' or p == '':
                continue
            if p == '..':
                moveUpCount += 1
                continue
            if moveUpCount > 0:
                moveUpCount -= 1
                continue
            if res == '':
                res = p
                continue

            res = p + "/" + res

        return "/" + res


class TestSolution(TestCase):
    def test_simplifyPath(self):
        test_cases = [
            {
                "name": "/home/",
                "str": "/home/",
                "expected": "/home"
            },
            {
                "name": "/../",
                "str": "/../",
                "expected": "/"
            },
            {
                "name": "/home//foo/",
                "str": "/home//foo/",
                "expected": "/home/foo"
            },
            {
                "name": "/a/./b/../../c/",
                "str": "/a/./b/../../c/",
                "expected": "/c"
            },
            {
                "name": "/a//b////c/d//././/..",
                "str": "/a//b////c/d//././/..",
                "expected": "/a/b/c"
            }
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.simplifyPath(testcase["str"]),
                             testcase["name"])
