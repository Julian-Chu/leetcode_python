class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):
        if not arrs:
            return 0
        nums_dict = {}
        count = 0

        for arr in arrs:
            for num in arr:
                nums_dict[num] = nums_dict.get(num, 0) + 1
                if nums_dict[num] == len(arrs):
                    count += 1

        return count


class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):
        if not arrs:
            return 0
        if len(arrs) == 1:
            return len(arrs[0])

        interesection = {num: 1 for num in arrs[0]}

        ans = 0
        n = len(arrs)
        for i in range(1, len(arrs)):
            for num in arrs[i]:
                if num in interesection:
                    interesection[num] += 1
                    if interesection[num] == n:
                        ans += 1

        return ans