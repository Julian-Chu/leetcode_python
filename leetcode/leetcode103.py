from typing import List

from helper import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = self.BuildLevelOrder(root, [], 0)
        return res

    def BuildLevelOrder(self, root, res: List[List[int]], level) -> List[List[int]]:
        if not root:
            return res

        if len(res) == level:
            res.append([])

        if level%2==0:
            res[level].append(root.val)
        else:
            res[level].insert(0,root.val)
        res = self.BuildLevelOrder(root.left, res, level + 1)
        res = self.BuildLevelOrder(root.right, res, level + 1)
        return res
