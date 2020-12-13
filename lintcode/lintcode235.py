
"""
一般作法，將num除到沒有該質因數
常見問題:  忘記最後一個質因數，該質因數大於up
"""
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        up = int(num ** 0.5 + 1)

        factors = []

        for i in range(2, up):
            while num % i == 0:
                num //= i
                factors.append(i)

        if num != 1:
            factors.append(num)

        return factors


"""
另類作法: 將小於num平方根的質數先取出，再進行運算
常見問題:  忘記最後一個質因數，該質因數大於up，怎麼有效率取出質數
"""
import math
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        up = int(math.sqrt(num)) + 1  # num**0.5+1
        f = [0] * up
        prime = []
        for i in range(2, up):
            if f[i] == 0:
                prime.append(i)
                for j in range(i * i, up, i):
                    f[j] = 1

        rt = []
        for a in prime:
            while num % a == 0:
                rt.append(a)
                num //= a  # num /=a : return is float, not int
        if num != 1:
            rt.append(num)

        return rt