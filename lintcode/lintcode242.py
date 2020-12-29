"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

"""
BFS
"""
from collections import deque

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if not root:
            return []

        queue = deque([root])
        lists = []
        dummy = ListNode(0)
        while queue:
            dummy.next = 0
            tail = dummy
            for i in range(len(queue)):
                node = queue.popleft()
                tail.next = ListNode(node.val)
                tail = tail.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            lists.append(dummy.next)

        return lists

"""
DFS
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        result = []
        self.dfs(root, 1, result)
        return result

    def dfs(self, root, depth, result):
        if not root:
            return
        node = ListNode(root.val)
        if depth > len(result):
            result.append(node)
        else:
            node.next = result[depth - 1]
            result[depth - 1] = node

        self.dfs(root.right, depth + 1, result)
        self.dfs(root.left, depth + 1, result)