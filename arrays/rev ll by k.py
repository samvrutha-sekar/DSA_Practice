class Solution:
    def reverseKGroup(self, head, k):
        if not head or k <= 1:
            return head

        curr = head
        prev = None
        count = 0

        # Check whether k nodes are available
        temp = head
        for i in range(k):
            if not temp:
                return head
            temp = temp.next

        # Reverse k nodes
        while count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        # Recursively reverse the remaining groups
        head.next = self.reverseKGroup(curr, k)

        return prev