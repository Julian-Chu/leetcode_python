# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        rootVal = max(nums)
        rootIdx = nums.index(rootVal)

        root = TreeNode(rootVal)
        root.left = self.constructMaximumBinaryTree(nums[:rootIdx])
        root.right = self.constructMaximumBinaryTree(nums[rootIdx + 1:])

        return root