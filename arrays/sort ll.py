class Solution:
    def sortList(self, head):
        count = [0, 0, 0]
        temp = head

        # Count 0s, 1s and 2s
        while temp:
            count[temp.data] += 1
            temp = temp.next

        temp = head

        # Replace the node values in sorted order
        i = 0
        while temp:
            if count[i] > 0:
                temp.data = i
                count[i] -= 1
            else:
                i += 1
                continue

            temp = temp.next

        return head