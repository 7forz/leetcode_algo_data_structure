class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums_mixed = [0] * (len(nums1)+len(nums2))
        j = k = 0  # j for nums1, k for nums2
        for i in range(len(nums_mixed)):
            try:
                if nums1[j] <= nums2[k]:
                    nums_mixed[i] = nums1[j]
                    j += 1
                else:
                    nums_mixed[i] = nums2[k]
                    k += 1
            except IndexError:
                if j == len(nums1):  # nums1 is empty
                    nums_mixed[i:] = nums2[k:]
                    break
                else:  # nums2 is empty
                    nums_mixed[i:] = nums1[j:]
                    break
            
        mid = len(nums_mixed)//2
        if len(nums_mixed) % 2:  # 1 number
            return nums_mixed[mid]
        else:  # 2 numbers
            return (nums_mixed[mid-1]+nums_mixed[mid])/2.0