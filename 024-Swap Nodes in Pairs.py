# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        
        # length > 1
        _head = ListNode(None)
        _head.next = head.next  # 首次调换
        now = head
        while now:
            if now.next:
                if now.next.next:
                    a, b, c = now, now.next, now.next.next
                    if c.next:
                        a.next = c.next
                    else:
                        a.next = c
                    b.next = a
                    now = c
                else:  # a -> b -> None
                    a, b = now, now.next
                    a.next = b.next
                    b.next = a
                    break
            else:
                break
        return _head.next