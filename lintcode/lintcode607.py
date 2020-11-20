class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    nums = []

    def add(self, number):
        self.nums.append(number)
        self.nums.sort()

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        nums = self.nums
        start, end = 0, len(nums) - 1

        while start < end:
            two_sum = nums[start] + nums[end]
            if two_sum > value:
                end -= 1
            elif two_sum < value:
                start += 1
            else:
                return True

        return False