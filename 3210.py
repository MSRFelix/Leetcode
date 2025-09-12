class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        l = len(s)
        double = s + s
        if k > l:
            new_k = k % l
        else:
            new_k = k
        sol = ""
        for i in range(l):
            sol += double[i+new_k]
        return sol

# encrypting a string, almost like the Caesar's Code 
