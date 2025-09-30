class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min1 = float('inf')
        min2 = float('inf')
        for i in range(len(nums1)):
            if nums1[i] < min1:
                min1 = nums1[i]
            if nums2[i] < min2:
                min2 = nums2[i]
        return min2 - min1

# 3131 difference between two arrays
