# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0

        base = 1
        while l1:
            num1 += l1.val*base
            base *= 10
            l1 = l1.next

        base = 1
        while l2:
            num2 += l2.val*base
            base *= 10
            l2 = l2.next
        
        result = num1 + num2
        result_listnode = ListNode(result % 10)
        pointer = result_listnode
        result = result // 10  # right move 1 digit
        while result>0:
            new_listnode = ListNode(result % 10)
            result = result // 10
            pointer.next = new_listnode
            pointer = new_listnode
        
        return result_listnode

# a=Solution()
# a.addTwoNumbers(l1,l2)