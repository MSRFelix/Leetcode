class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(0, len(grid)):
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] < 0:
                    c+= 1
                else:
                    break
        return c

# 1351: Count negative numbers in matrix
