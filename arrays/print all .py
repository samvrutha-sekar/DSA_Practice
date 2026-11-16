
from collections import deque

class Solution:
    def distanceK(self, root, target, k):

        parent = {}

        def markParents(node, par):
            if not node:
                return

            parent[node] = par
            markParents(node.left, node)
            markParents(node.right, node)

        markParents(root, None)

        q = deque([target])
        visited = {target}
        distance = 0

        while q:
            if distance == k:
                break

            for _ in range(len(q)):
                node = q.popleft()

                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            distance += 1

        return [node.data for node in q]
