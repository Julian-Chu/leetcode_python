class Solution: # doubly linked list
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        if not nums:
            return -1

        key_to_prevNode = {}
        dummy_head = Node(0)
        dummy_tail = Node(0)
        dummy_head.next = dummy_tail
        dummy_tail.prev = dummy_head
        unique_hash = {}
        duplicate_set = set()

        for num in nums:
            if num in duplicate_set:
                continue

            if num in unique_hash:
                node = unique_hash.pop(num)
                duplicate_set.add(num)
                self.remove_node(node)
                continue

            new_node = Node(num)
            self.add_node_to_end(new_node, dummy_tail)
            unique_hash[num] = new_node

            if num == number:
                if dummy_head.next:
                    return dummy_head.next.val
        return -1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def add_node_to_end(self, node, dummy_tail):
        prev = dummy_tail.prev
        prev.next = node
        node.prev = prev
        node.next = dummy_tail
        dummy_tail.prev = node


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if num == number:
                break
        else:
            return -1

        for num in nums:
            if counter[num] == 1:
                return num
            if num == number:
                break

        return -1