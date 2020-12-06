class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        uglys = [1]

        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            last_number = uglys[i - 1]
            while uglys[p2] * 2 <= last_number:
                p2 += 1
            while uglys[p3] * 3 <= last_number:
                p3 += 1
            while uglys[p5] * 5 <= last_number:
                p5 += 1

            uglys.append(min(
                uglys[p2] * 2,
                uglys[p3] * 3,
                uglys[p5] * 5
            ))

        return uglys[n - 1]