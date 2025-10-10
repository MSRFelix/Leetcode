class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sol1, sol2 = 0, 0
        s1 = set(nums1)
        s2 = set(nums2)
        for i in nums1:
            if i in s2:
                sol1 += 1
        for i in nums2:
            if i in s1:
                sol2 += 1
        return [sol1, sol2]

#  count nums1[i] in nums2 and vice versa  
