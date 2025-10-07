class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = licensePlate.lower()
        lp2 = ""
        for i in lp:
            if i.islower():
                lp2 += i
        def compare(w1, w2):
            hashmap = {}
            for i in w1:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    hashmap[i] = 1
            for i in w2:
                if i in w1:
                    hashmap[i] -= 1
                    if hashmap[i] < 0:
                        return -1
                else:
                    return -1
            return len(w1)
        mini = float('inf')
        sol = words[0]
        for i in words:
            x = compare(i.lower(), lp2)
            if x < mini and x != -1:
                mini = x
                sol = i
        return sol


# shortest word to recreate all the letters of licensePlate
