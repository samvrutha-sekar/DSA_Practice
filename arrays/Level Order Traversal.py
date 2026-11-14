from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        q = deque([root])
        ans = []

        while q:
            n = len(q)
            level = []

            for _ in range(n):
                node = q.popleft()
                level.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)

        return ans