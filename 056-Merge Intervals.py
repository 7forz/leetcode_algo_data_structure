class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge_two(interval_a: List[int], interval_b: List[int]) -> List[List[int]]:
            """
                interval_a: [a, b]. interval_b: [c, d]
                where a < c

                [1,2], [3,4] -> [[1,2], [3,4]]   circumstance 1
                [1,3], [2,4] -> [[1,4]]          circumstance 2
                [1,4], [2,3] -> [[1,4]]          circumstance 3
            """
            result = []
            if interval_a[1] < interval_b[0]:  # circumstance 1
                return [interval_a, interval_b]
            elif interval_a[1] < interval_b[1]:  # circumstance 2
                return [[interval_a[0], interval_b[1]]]
            elif interval_a[1] >= interval_b[1]:  # circumstance 3
                return [interval_a]
            else:
                1/0  # impossible

        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0])

        result = [intervals[0]]
        for interval in intervals[1:]:
            merged = merge_two(result[-1], interval)
            if len(merged) == 1:
                result[-1] = merged[0]
            else:
                result.append(merged[1])
        
        return result
