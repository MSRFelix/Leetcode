class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = len(s)
        sol = [([0] * l) for i in range(numRows)]
        sol_str = ""
        i = 0
        j = 0
        k = 0
        while i < len(s):
            while j < numRows and i < l:
                sol[j][k] = s[i]
                j+=1
                i+=1
            j-=  2 
            k+= 1
            while j >= 0 and i < l:
                sol[j][k] = s[i]
                j -= 1
                k += 1
                i += 1
            j+= 2
            k -= 1
        i = 0
        j = 0
        for i in range(len(sol)):
            for j in range(len(sol[0])):
                if sol[i][j] != 0:
                    sol_str += sol[i][j]
        return sol_str

one = Solution()
sent = "AB"
print(one.convert(sent, 1))

# rearranging string in a zig zag manner
