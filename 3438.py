class Solution:
    def findValidPair(self, s: str) -> str:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in range(1, len(s)):
            if s[i] != s[i-1] and s[i] == str(hashmap[s[i]]) and s[i-1] == str(hashmap[s[i-1]]):
                    return s[i-1] + s[i]
        return ""
        
# 3438 string checking for valid adjacent pairs
