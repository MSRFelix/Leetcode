class Solution:
    seen = {}
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        elif n in self.seen:
            return self.seen[n]
        else:
            self.seen[n-3] = self.tribonacci(n-3)
            return (self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3))
    
# tribonacci: first dynamic programming attempt: Memoization + recursion
