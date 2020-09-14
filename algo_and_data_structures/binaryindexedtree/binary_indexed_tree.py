import random


class BinaryIndexedTree:
    #def __init__(self, init_list: list):
    #    self._array = [0] * (len(init_list) + 1)
    #    for i, value in enumerate(init_list):
    #        self.update(i, value)

    def __init__(self, init_list: list):
        """ initialize in O(n) """
        self._array = [0] + init_list
        for index in range(1, len(self._array)):
            j = index + self._lsb(index)
            if j < len(self._array):
                self._array[j] += self._array[index]

    def __len__(self):
        """ 内部处理时长度加一，减一后对外部的长度才不变 """
        return len(self._array) - 1

    @staticmethod
    def _lsb(n: int) -> int:
        return n & (-n)

    def _prefix_sum(self, index: int):
        index += 1
        result = 0
        while index != 0:
            result += self._array[index]
            index -= self._lsb(index)
        return result

    def range_sum(self, start: int, end: int):
        """ 计算数组 [start, end] 闭区间的和 """
        return self._prefix_sum(end) - self._prefix_sum(start - 1)

    def update(self, index: int, delta):
        index += 1
        while index < len(self._array):
            self._array[index] += delta
            index += self._lsb(index)


if __name__ == "__main__":
    MAX = 10000
    LENGTH = 1000

    test_data = [random.randint(1, MAX) for _ in range(LENGTH)]

    binary_indexed_tree = BinaryIndexedTree(test_data)

    print(f'the sum of [12, 345] is {sum(test_data[12:346])} (by simple addition)')
    print(f'the sum of [12, 345] is {binary_indexed_tree.range_sum(12, 345)} (by binary indexed tree)')

    # 随便找10个元素，各加上随机值
    for _ in range(10):
        random_index = random.randint(0, LENGTH-1)
        random_delta = random.randint(1, MAX)
        test_data[random_index] += random_delta
        binary_indexed_tree.update(random_index, random_delta)

    print('\nafter updating some data')
    print(f'the sum of [123, 666] is {sum(test_data[123:667])} (by simple addition)')
    print(f'the sum of [123, 666] is {binary_indexed_tree.range_sum(123, 666)} (by binary indexed tree)')
