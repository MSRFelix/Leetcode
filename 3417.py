class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        c = 0
        sol = []
        for i in range(len(grid)):
            if i % 2 == 0:
                for j in range(len(grid[0])):
                    if c % 2 == 0:
                        sol.append(grid[i][j])
                    c += 1
            else:
                 for j in range(len(grid[0])-1, -1, -1):
                    if c % 2 == 0:
                        sol.append(grid[i][j])
                    c += 1
        return sol

# matrix traversal in zig zag pattern
