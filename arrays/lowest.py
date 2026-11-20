
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None

        if root.data == p.data or root.data == q.data:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        return right
