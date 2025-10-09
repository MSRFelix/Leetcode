class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if z > x:
            d1 = z-x
        else:
            d1 = x - z
        if z > y:
            d2 = z-y
        else:
            d2 = y - z
        if d1 > d2:
            return 2
        elif d2 > d1:
            return 1
        else:
            return 0

# number comparison
