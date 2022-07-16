from typing import (
    List,
)

class Solution:
    def __init__(self):
        self.count = {}
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            if target - num in self.count:
                return [self.count[target-num], i]
            self.count[num] = i
        return [-1, -1]
