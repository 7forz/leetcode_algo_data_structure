# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # not a good idea because of O(n) memory comsumption,
        # should use 2 pointers to locate the Nth from end
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        
        if n == 1:
            if len(nodes) == 1:
                return None
            else:
                nodes[-2].next = None
        elif n != len(nodes):
            nodes[-n-1].next = nodes[-n+1]  # remove Nth from end
        else:  # n == len(nodes)
            return head.next

        return head