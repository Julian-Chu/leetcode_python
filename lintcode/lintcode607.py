class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    nums = []

    def add(self, number):
        self.nums.append(number)
        self.nums.sort()   # best case: O(nlogn) , bubble sort is better in best case

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


class TwoSum:

    def __init__(self):
        self.nums = []

    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        self.nums.append(number)
        index = len(self.nums) - 1
        while index > 0 and self.nums[index - 1] > self.nums[index]:
            self.nums[index], self.nums[index - 1] = self.nums[index - 1], self.nums[index]
            index -= 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        left, right = 0, len(self.nums) - 1
        while left < right:
            two_sum = self.nums[left] + self.nums[right]
            if two_sum < value:
                left += 1
            elif two_sum > value:
                right -= 1
            else:
                return True
        return False


class TwoSum:

    def __init__(self):
        self.counter = {}

    """
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        self.counter[number] = self.counter.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        for num in self.counter:
            if value - num == num:
                return self.counter[num] >= 2
            if self.counter.get(value - num, 0) > 0:
                return True
        return False