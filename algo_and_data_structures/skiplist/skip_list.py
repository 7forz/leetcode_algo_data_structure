import random
import time
from typing import List


class Node:
    __slots__ = ('value', 'next', 'dense')
    def __init__(self, value, next = None):
        self.value = value
        self.next: Node = next
        self.dense: Node = None  # 指向更底层的同值节点


# 给每个Node编号，方便debug
# class Node:
#     number = 1
#     def __init__(self, value, next = None):
#         self.id = Node.number
#         Node.number += 1
#         self.value = value
#         self.next: Node = next
#         self.dense: Node = None  # 指向更底层的同值节点

#     def __repr__(self):
#         return f'(#{self.id}, value: {self.value}, ' \
#             f'→: #{self.next.id if self.next else None}, ↓: #{self.dense.id if self.dense else None})'


class SkipList:
    """
        使用跳表维护一个 查找(判断存在性)、添加、删除 的平均时间都是O(log n)的 自排序链表

        实际上是多层的链表，底层是完整的链表，越上层的链表越稀疏
    """
    _ROOT = object()  # 为了不使用哨兵节点，定义一个特殊值，该值视作比任何值都小

    def __init__(self):
        self.size = 0
        self.roots: List[Node] = [Node(self._ROOT)]  # 初始为1层root节点

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return str(self)

    def to_list(self):
        """ 只返回底层密链表的数据 """
        result = []
        node = self.roots[0].next
        while node:
            result.append(node.value)
            node = node.next
        return result

    def __contains__(self, val):
        memory_nodes = self._find(val)
        if memory_nodes[-1].next.value == val:
            return True
        return False

    # def debug(self):
    #     for root in self.roots[::-1]:
    #         result = []
    #         node = root.next
    #         while node:
    #             result.append(repr(node))
    #             node = node.next
    #         print(result)
    #     print()

    def _insert_node(self, new_node: Node, prev: Node):
        """ 使
            prev -> prev_next
            变成
            prev -> new_node -> prev_next
        """
        original_next = prev.next
        new_node.next = original_next
        prev.next = new_node

    def _remove_node(self, to_remove: Node, prev: Node):
        """ 使
            prev -> to_remove -> to_remove_next
            变成
            prev -> to_remove_next
        """
        prev.next = to_remove.next
        del to_remove

    def _find(self, val) -> List[Node]:
        """ 由顶层的root节点向较密层搜索给定的val，并由顶至底记录标红的节点 """
        memory_nodes: List[Node] = []

        i = len(self.roots) - 1  # 顶层的root节点
        current_node = self.roots[i]

        # 搜索高层的节点，记录往下移动的节点
        while i > 0 and (current_node.value is self._ROOT or val > current_node.value):
            while current_node.next and val > current_node.next.value:
                current_node = current_node.next
            memory_nodes.append(current_node)
            current_node = current_node.dense
            i -= 1

        # 搜索底层的节点，记录刚好小于val的节点
        while current_node.next and val > current_node.next.value:
            current_node = current_node.next
        memory_nodes.append(current_node)

        return memory_nodes

    def add(self, val):
        # print('add', val)  ################################ debug
        self.size += 1

        # 找到标红的节点
        memory_nodes = self._find(val)

        # 首先在底层插入节点，这是100%插入的
        new_node = Node(val)
        self._insert_node(new_node=new_node, prev=memory_nodes.pop())  #从底层开始pop
        current_node = new_node

        # 然后随机决定是否向上层添加相同值节点作为索引
        current_level = 1  # 底层的level是0，1即上一层
        while random.random() > 0.5:
            # 新建节点，确定dense的指向
            upper_node = Node(val)
            upper_node.dense = current_node

            current_level += 1
            if current_level <= len(self.roots):  # 不用加新的层，在之前搜索的节点之后添加节点
                self._insert_node(new_node=upper_node, prev=memory_nodes.pop())
            else:  # 加新的层有2个节点： root节点 -> 新节点(upper_node) -> None
                new_root_node = Node(self._ROOT, next=upper_node)  # 新的root节点
                new_root_node.dense = self.roots[current_level-2]
                self.roots.append(new_root_node)
                break
            current_node = upper_node

    def remove(self, val):
        """ 找到标红的节点，然后检查这些节点的next是否等于val，相等则删除，并处理可能的空层 """
        if val not in self:
            raise ValueError(f'{val} not in this skip list')

        memory_nodes = self._find(val)
        for node in memory_nodes:  # 从上层往下层
            if node.next and node.next.value == val:
                self._remove_node(node.next, node)
        
        # 从上层往下层，检查是否有层被清空，有则把该层的root节点也清除，底层的除外
        for i in range(len(self.roots)-1, 0, -1):
            if self.roots[i].next is None:
                self.roots.pop(i)


if __name__ == "__main__":
    MAX = 999999999
    LENGTH = 100000
    # random.seed(1234)

    skip_list = SkipList()

    test_data = [random.randint(1, MAX) for _ in range(LENGTH)]

    t1 = time.perf_counter()
    for num in test_data:
        skip_list.add(num)
    t2 = time.perf_counter()
    # skip_list.debug()  # 可以debug看一下

    test_data_sorted = sorted(test_data)
    print('correct:', str(test_data_sorted) == str(skip_list))
    print('add time cost:', t2-t1)

    ##############################
    t3 = time.perf_counter()
    data_to_remove = test_data[:LENGTH//2]  # 抽前面一半的数来删除
    for num in data_to_remove:
        skip_list.remove(num)
    t4 = time.perf_counter()

    test_data_remaining_sorted = sorted(test_data[LENGTH//2:])
    print('correct:', str(test_data_remaining_sorted) == str(skip_list))
    print('remove time cost:', t4-t3)

    # LENGTH比较大的话，下面相当慢

    # print('=============================================')
    # def insert_to_list(_list: list, val):
    #     """ 按大小插入列表，保证插入前和插入后列表均有序 """
    #     if not _list:
    #         _list.append(val)
    #     else:
    #         i = 0
    #         length = len(_list)
    #         while i <= length - 1 and _list[i] < val:
    #             i += 1
    #         _list.insert(i, val)
    
    # python_list = []

    # t5 = time.perf_counter()
    # for num in test_data:
    #     insert_to_list(python_list, num)
    # t6 = time.perf_counter()

    # print('correct:', str(test_data_sorted) == str(python_list))
    # print('add time cost slow version:', t6-t5)
