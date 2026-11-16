from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root):

        nodes = defaultdict(list)
        q = deque([(root, 0, 0)])

        while q:
            node, row, col = q.popleft()

            if node:
                nodes[col].append((row, node.data))

                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))

        ans = []

        for col in sorted(nodes):
            values = sorted(nodes[col])
            ans.append([val for row, val in values])

        return ans
