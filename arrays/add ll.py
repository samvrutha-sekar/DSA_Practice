class Solution:
    def addTwoNumbers(self, linkedList1, linkedList2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while linkedList1 or linkedList2 or carry:
            x = linkedList1.data if linkedList1 else 0
            y = linkedList2.data if linkedList2 else 0

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if linkedList1:
                linkedList1 = linkedList1.next
            if linkedList2:
                linkedList2 = linkedList2.next

        return dummy.next