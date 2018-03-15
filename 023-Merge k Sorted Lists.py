# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        root = ListNode(None)
        p = root
        heap_nums = []

        for i in range(len(lists)):   # 第1次建堆
            if lists[i]:
                heapq.heappush(heap_nums, (lists[i].val, i))

        while heap_nums:
            value, index = heapq.heappop(heap_nums)
            node = ListNode(value)
            lists[index] = lists[index].next
            p.next = node
            p = node
            if lists[index]:
                heapq.heappush(heap_nums, (lists[index].val, index))

        return root.next  # root仅作哨兵