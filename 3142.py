class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(1, len(grid[0])):
            if grid[0][i] == grid[0][i-1]:
                return False
        for i in range(1, len(grid)):
            if grid[0] != grid[i]:
                return False
        return True

# 3142 check if grid[][] equal to number below it, but unequal to number to
# the right; one loop to check to the right, one for below


