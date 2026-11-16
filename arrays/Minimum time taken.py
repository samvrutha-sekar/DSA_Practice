
from collections import deque

class Solution:
    def timeToBurnTree(self, root, start):

        parent = {}
        target = None

        def markParents(node, par):
            nonlocal target

            if not node:
                return

            parent[node] = par

            if node.data == start:
                target = node

            markParents(node.left, node)
            markParents(node.right, node)

        markParents(root, None)

        q = deque([target])
        visited = {target}
        time = -1

        while q:
            size = len(q)
            time += 1

            for _ in range(size):
                node = q.popleft()

                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        return time
