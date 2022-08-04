class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        count = 0
        maxCount = 0
        prev = None

        def traverse(cur: TreeNode):
            nonlocal prev, count, maxCount, res
            if not cur:
                return

            traverse(cur.left)
            if prev and cur.val == prev.val:
                count += 1
            else:
                count = 1

            prev = cur
            if count > maxCount:
                maxCount = count
                res.clear()
                res.append(cur.val)
            elif count == maxCount:
                res.append(cur.val)

            traverse(cur.right)

        traverse(root)
        return res