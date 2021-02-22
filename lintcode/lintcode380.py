class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        tailA = headA

        while tailA.next:
            tailA = tailA.next

        tailA.next = headB

        slow, fast = headA, headA
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = headA
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                tailA.next = None
                return slow
        return None


"""
a 走 a+c+b距離
b 走 b+c+a距離
相遇為交點或None
環狀結構

"""
class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


"""
extra space O(n)
"""
class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        hashset = set()

        while headA:
            hashset.add(headA)
            headA = headA.next

        while headB:
            if headB in hashset:
                return headB
            headB = headB.next

        return None

