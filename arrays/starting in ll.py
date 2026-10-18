class Solution:
    def findStartingPoint(self, head):
        slow = head
        fast = head

        # Detect the loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they meet, a loop exists
            if slow == fast:
                slow = head

                # Find the starting point of the loop
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None