class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        sol = events[0][0]
        maxi = events[0][1]
        for i in range(1, len(events)):
            if events[i][1] - events[i-1][1] > maxi:
                maxi = events[i][1] - events[i-1][1]
                sol = events[i][0]
            elif events[i][1] - events[i-1][1] == maxi:
                if events[i][0] < sol:
                    sol = events[i][0]
        return sol

# longest Push time of Button
