# golang slice concept
class RandomizedSet:

    def __init__(self):
        self.random_set = {}
        self.array = []
        self.array_end = -1

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        if val in self.random_set:
            return False

        self.array_end += 1
        if len(self.array) - 1 >= self.array_end:
            self.array[self.array_end] = val
        else:
            self.array.append(val)
        self.random_set[val] = self.array_end
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        if val not in self.random_set:
            return False

        val_index = self.random_set.pop(val)
        last_val_in_array = self.array[self.array_end]
        self.array[val_index] = last_val_in_array
        self.random_set[last_val_in_array] = val_index
        self.array_end -= 1
        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        import random
        index = random.randint(0, self.array_end)
        return self.array[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()

import random

"""
random.seed()
random.choice(list)
"""
class RandomizedSet:

    def __init__(self):
        self.val2index = {}
        self.vals = []
        random.seed()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        if val in self.val2index:
            return False
        self.val2index[val] = len(self.vals)
        self.vals.append(val)
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        vals, val2index = self.vals, self.val2index
        if val not in val2index:
            return False

        index = val2index[val]
        if index < len(vals) - 1:
            last = vals[-1]
            val2index[last] = index
            vals[index] = last
        del val2index[val]
        vals.pop()

        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        return random.choice(self.vals)

import random

# use array.pop()
class RandomizedSet:

    def __init__(self):
        self.nums, self.val2index = [], {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        if val in self.val2index:
            return False

        self.nums.append(val)
        self.val2index[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        if val not in self.val2index:
            return False

        index = self.val2index[val]
        last = self.nums[-1]

        self.nums[index] = last
        self.val2index[last] = index

        self.nums.pop()
        del self.val2index[val]
        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
