from random import randint, seed


class Solution:

    def __init__(self, intervalCount, virtualNodeCount):
        self.virtualNodeCount = virtualNodeCount
        self.intervalCount = intervalCount
        self.circumference = [-1 for _ in range(intervalCount)]

    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """

    @classmethod
    def create(cls, n, k):
        return cls(n, k)

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """

    def addMachine(self, machine_id):
        seed(1)
        newNodes = []
        for _ in range(self.virtualNodeCount):
            nodeId = randint(0, self.intervalCount - 1)
            while self.circumference[nodeId] != -1:
                nodeId = randint(0, self.intervalCount - 1)
            self.circumference[nodeId] = machine_id
            newNodes.append(nodeId)

        return newNodes

    """
    @param: hashcode: An integer
    @return: A machine id
    """

    def getMachineIdByHashCode(self, hashcode):
        nodeId = hashcode % self.intervalCount
        while self.circumference[nodeId] == -1:
            nodeId += 1
            nodeId %= self.intervalCount

        return self.circumference[nodeId]




class Solution:

    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """

    @classmethod
    def create(cls, n, k):
        solution = cls()
        solution.ids = {}
        solution.machines = {}
        solution.n = n
        solution.k = k
        return solution
    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """

    def addMachine(self, machine_id):
        ids = []
        import random
        for i in range(self.k):
            index = random.randint(0, self.n-1)
            while index in self.ids:
                index = random.randint(0, self.n - 1)

            ids.append(index)
            self.ids[index] = True

        ids.sort()
        self.machines[machine_id] = ids
        return ids


    """
    @param: hashcode: An integer
    @return: A machine id
    """

    def getMachineIdByHashCode(self, hashcode):
        machine_id = -1
        distance = self.n + 1

        for key, machine_ids in self.machines.items():
            import bisect
            index = bisect.bisect_left(machine_ids, hashcode) % len(machine_ids)
            d = machine_ids[index] - hashcode
            if d < 0:
                d += self.n

            if d < distance:
                distance = d
                machine_id = key

        return machine_id
