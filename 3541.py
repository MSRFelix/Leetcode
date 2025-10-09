class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = 0
        k = 0
        dict = ("a", "e", "i", "o", "u")
        vowels = {}
        cons = {}
        for i in s:
            if i in dict:
                if i in vowels:
                    vowels[i] += 1
                else:
                    vowels[i] = 1
            elif i in cons:
                cons[i] += 1
            else:
                cons[i] = 1
        for i, j in vowels.items():
            if j > v:
                v = j
        for i, j in cons.items():
            if j > k:
                k = j
        return v + k

# finding most frequent vowel and consonant in String
