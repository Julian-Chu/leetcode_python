class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)

        return self.merge_two_lists(left, right)

    def merge_two_lists(self, a, b):
        dummyNode = cur = ListNode(-1)
        while a and b:
            if a.val < b.val:
                cur.next = a
                a = a.next
            else:
                cur.next = b
                b = b.next
            cur = cur.next

        while a:
            cur.next = a
            cur = cur.next
            a = a.next

        while b:
            cur.next = b
            cur = cur.next
            b = b.next
        return dummyNode.next


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])

        k = len(lists)
        left = self.mergeKLists(lists[:k // 2])
        right = self.mergeKLists(lists[k // 2:])

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, a, b):
        dummy = ListNode(-1)
        head = dummy
        while a and b:
            if a.val < b.val:
                head.next = a
                a = a.next
            else:
                head.next = b
                b = b.next
            head = head.next

        if a:
            head.next = a

        if b:
            head.next = b
        return dummy.next


import heapq


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None
        heap = []
        dummy = ListNode(-1)
        tail = dummy

        for i in range(len(lists)):
            if lists[i]:
                # push arrs_index , for the edge case,  value of nodes are equal
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            _, arrs_index, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            next_node = node.next
            if next_node:
                heapq.heappush(heap, (next_node.val, arrs_index, next_node))

        return dummy.next