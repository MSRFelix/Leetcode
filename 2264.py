class Solution:
    def largestGoodInteger(self, num: str) -> str:
        sol = ""
        curr_max = "0"
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                if num[i] >= curr_max:
                    sol = num[i] * 3
                    curr_max = num[i]
        return sol 
      
# finding same three digits in a row in string
