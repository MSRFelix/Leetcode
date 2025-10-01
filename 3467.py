from collections import deque
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        sol = deque([])
        for i in nums:
            if i % 2 == 0:
                sol.appendleft(0)
            else:
                sol.append(1)
        return list(sol)

# sorting array by parity using stacks        
