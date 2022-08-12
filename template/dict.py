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

    def remove_key(self):
        my_dict = {}
        #  To delete a key regardless of whether it is in the dictionary, use the two-argument form of
        my_dict.pop('key', None)

        # To delete a key that is guaranteed to exist, you can also use
        del my_dict['key']

    def get_default(self):
        dict = {}
        # return None
        val = dict.get("key")
        # return default 0
        val = dict.get("key", 0)

    def methods(self):
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        x = car.items()
        # x = car.values()
        # x = car.keys

        print(x)  # before the change

        car["color"] = "red"

        print(x)  # after the change