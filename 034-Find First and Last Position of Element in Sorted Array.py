class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binsearch(array, target, not_found_return_low=False):

            low = 0
            high = len(array) - 1

            while low <= high:
                mid = (low + high) // 2

                if target > array[mid]:
                    low = mid + 1
                elif target < array[mid]:
                    high = mid - 1
                else:
                    return mid

            if not_found_return_low:
                return low
            else:
                return -1
        
        is_exist = binsearch(nums, target, not_found_return_low=False)
        if is_exist == -1:
            return [-1, -1]
        
        start_pos = binsearch(nums, target-0.5, not_found_return_low=True)
        end_pos = binsearch(nums, target+0.5, not_found_return_low=True) - 1  # note -1
        
        return [start_pos, end_pos]