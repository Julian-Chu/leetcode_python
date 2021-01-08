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