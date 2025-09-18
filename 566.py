class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        sol = []
        k = 0
        curr = []
        if r*c != len(mat)*len(mat[0]):
            return mat
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                curr.append(mat[i][j])
                k += 1
                if k == c:
                    sol.append(curr.copy())
                    curr = []
                    k = 0
        return sol

# reshaping a matrix into other dimensions of size r * c
