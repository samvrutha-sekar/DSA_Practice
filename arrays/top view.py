class Solution:
    def topView(self, root):
        if not root:
            return []

        q = [(root, 0)]
        mp = {}

        while q:
            node, hd = q.pop(0)

            if hd not in mp:
                mp[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        return [mp[i] for i in sorted(mp)]