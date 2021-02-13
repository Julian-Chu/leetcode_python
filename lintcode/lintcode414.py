"""
O(log(dividend/ divisor))
"""
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """

    def divide(self, dividend, divisor):
        is_negative = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1

        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0
        while dividend >= divisor:
            tmp = divisor
            cnt = 1
            while dividend >= tmp:
                dividend -= tmp
                ans += cnt
                tmp = tmp << 1
                cnt = cnt << 1

        ans = ans * is_negative
        if ans > (1 << 31) - 1:
            return (1 << 31) - 1

        if ans < (-1 << 31):
            return -1 << 31

        return ans


class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """

    def divide(self, dividend, divisor):
        is_negative = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1

        ans = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0
        while dividend >= divisor:
            tmp = divisor
            cnt = 1
            while dividend >= tmp:
                tmp = tmp << 1
                cnt = cnt << 1

            tmp = tmp >> 1
            cnt = cnt >> 1
            dividend -= tmp
            ans += cnt
        ans = ans * is_negative
        if ans > (1 << 31) - 1:
            return (1 << 31) - 1

        if ans < (-1 << 31):
            return -1 << 31

        return ans