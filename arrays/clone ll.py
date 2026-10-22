class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}
        curr = head

        # Create copies of all nodes
        while curr:
            old_to_new[curr] = type(curr)(curr.val)
            curr = curr.next

        # Connect next and random pointers
        curr = head
        while curr:
            clone = old_to_new[curr]

            clone.next = old_to_new.get(curr.next)
            clone.random = old_to_new.get(curr.random)

            curr = curr.next

        return old_to_new[head]