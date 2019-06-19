class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # try:
        #     return nums.index(target)
        # except:
        #     return -1
        
        if not nums: return -1
        
        return self.find(nums, 0, len(nums)-1, target)
        
    def find(self, array, low, high, target):
        mid = (low + high) // 2
        
        if array[low] == target: return low
        if array[mid] == target: return mid
        if array[high] == target: return high
        
        if array[low] < target < array[mid]:  # sorted
            return self.find(array, low+1, mid-1, target)
        if array[mid] < target < array[high]:  # sorted
            return self.find(array, mid+1, high-1, target)
        
        if array[mid] > array[high] and (target < array[high] or target > array[mid]):
            return self.find(array, mid+1, high-1, target)
        
        if array[low] > array[mid] and (target > array[low] or target < array[mid]):
            return self.find(array, low+1, mid-1, target)
        
        return -1