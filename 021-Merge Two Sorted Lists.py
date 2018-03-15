class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        p = root
        while l1 or l2:
            if not l1:
                node = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                node = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            p.next = node
            p = node
        return root.next  # root仅作哨兵