class RandomizedCollection(object):

    def __init__(self):
        self.data = []
        self.dict = dict()

    def insert(self, val):
        flag = True
        if val not in self.dict:
            self.dict[val] = set()
            flag = False
        index = len(self.data)
        self.data.append(val)
        self.dict[val].add(index)
        return flag

    def remove(self, val):
        if val not in self.dict:
            return False

        index = self.dict[val].pop()
        last_index = len(self.data) - 1
        last_element = self.data[-1]

        if last_index != index:
            self.dict[last_element].remove(last_index)

        self.dict[last_element].add(index)
        self.data[index] = last_element
        self.data.pop()

        if not self.dict[val]:
            del self.dict[val]
        return True

    def getRandom(self):
        import random
        idx = random.randint(0, len(self.data) - 1)
        return self.data[idx]


"""
getRandom is not O(1) failed
"""
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums_dict = {}
        self.count = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.count += 1
        if val not in self.nums_dict:
            self.nums_dict[val] = 1
            return True
        else:
            self.nums_dict[val] += 1
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nums_dict:
            self.nums_dict[val] -= 1
            if self.nums_dict[val] == 0:
                del self.nums_dict[val]
            self.count -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        target = random.randint(1, self.count)
        cnt = 0
        for num in self.nums_dict:
            cnt += self.nums_dict[num]
            if cnt >= target:
                return num
        return None