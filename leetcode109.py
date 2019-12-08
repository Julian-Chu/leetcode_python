from helper import TreeNode, ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        preMid, mid, fast = head, head, head.next
        while fast is not None and fast.next is not None:
            preMid = mid
            mid = mid.next
            fast = fast.next.next
        node = TreeNode(mid.val)
        if mid != head:
            preMid.next = None
            node.left = self.sortedListToBST(head)

        node.right = self.sortedListToBST(mid.next)
        return node
