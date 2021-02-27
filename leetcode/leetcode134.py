from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remain, debt, start = 0, 0, 0

        for i in range(len(gas)):
            remain += gas[i] - cost[i]
            if remain < 0:
                start = i + 1
                debt += remain
                remain = 0

        if debt + remain < 0:
            return -1

        return start
