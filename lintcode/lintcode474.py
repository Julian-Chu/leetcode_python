class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        parents = set()

        while A:
            parents.add(A)
            A = A.parent

        while B:
            if B in parents:
                return B
            B = B.parent

        return None