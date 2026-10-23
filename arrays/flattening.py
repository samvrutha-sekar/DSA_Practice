class Solution:
    def flattenLinkedList(self, head):
        if head is None or head.next is None:
            return head

        mergedHead = self.flattenLinkedList(head.next)
        head.next = None

        return self.merge(head, mergedHead)

    def merge(self, list1, list2):
        dummyNode = ListNode(-1)
        res = dummyNode

        while list1 and list2:
            if list1.val <= list2.val:
                res.child = list1
                list1 = list1.child
            else:
                res.child = list2
                list2 = list2.child

            res = res.child
            res.next = None

        res.child = list1 if list1 else list2

        return dummyNode.child