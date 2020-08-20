from unittest import TestCase


class Solution:
    def isValid(self, s):
        stack = []
        parentheses_map = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in parentheses_map:
                stack.append(c)
            elif not stack or parentheses_map[c] != stack.pop():
                return False
        return not stack


class Test(TestCase):
    def test_is_valid(self):
        test_cases = [
            {
                "input": "()",
                "expected": True
            },

            {
                "input": "()[]{}",
                "expected": True
            },

            {
                "input": "(]",
                "expected": False
            },
        ]

        solution = Solution()
        for testcase in test_cases:
            self.assertEqual(testcase["expected"], solution.isValid(testcase["input"]))
