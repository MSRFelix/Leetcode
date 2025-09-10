class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashmap = {}
        sum = 0
        l = len(s)
        for i in range(l):
            hashmap[s[i]] = i
        for i in range(l):
            if hashmap[t[i]] > i:
                sum += hashmap[t[i]] - i
            else:
                sum += i - hashmap[t[i]]
        return sum

# sum of absolute differences of indices of chars
