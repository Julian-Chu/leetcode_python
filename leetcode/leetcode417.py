class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))

        return res
