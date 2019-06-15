# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not k:
            return head
        
        # get length first
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        
        k = k % length  # get the valid length
        if not k:  # rotate a full cycle
            return head
        
        # 即以倒数第k个节点作为新的头 把指向null的改为指向原来的头
        # find new head
        p = head
        nodes_to_go = length - k
        while nodes_to_go:
            if nodes_to_go == 1:
                new_tail = p
            p = p.next
            nodes_to_go -= 1
        new_head = p
        
        # find old tail
        while p.next:
            p = p.next
        # old tail's next is old head
        p.next = head

        # set new tail
        new_tail.next = None

        return new_head
