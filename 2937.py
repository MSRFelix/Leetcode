class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i = 0
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        l = min(l1, l2, l3)
        while i < l and s1[i] == s2[i] == s3[i]:
            i += 1
        if i == 0:
            return -1
        x = 0
        if i < l1:
            x += l1-i
        if i < l2:
            x += l2 - i
        if i < l3:
            x += l3 - i
        return x       

# string comp and changes to make all of them equal
