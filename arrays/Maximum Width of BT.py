from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        q = deque([(root, 0)])
        ans = 0

        while q:
            n = len(q)
            mini = q[0][1]
            first = last = 0

            for i in range(n):
                node, idx = q.popleft()
                idx -= mini

                if i == 0:
                    first = idx

                if i == n - 1:
                    last = idx

                if node.left:
                    q.append((node.left, 2 * idx + 1))

                if node.right:
                    q.append((node.right, 2 * idx + 2))

            ans = max(ans, last - first + 1)

        return ans