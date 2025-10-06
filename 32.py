class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        j = 0
        l = len(s)
        maxi = 0
        if l > 0 and s[0] == ")":
            while j < l and s[j] == ")":
                j+= 1
        if l > 0 and s[l-1] == "(":
            while l > 0 and s[l-1] == "(":
                l -= 1
        while j < l:
            if maxi > l-j:
                break
            open = 0
            for k in range(j, len(s)):
                if s[k] == "(":
                    open += 1
                    continue
                else:
                    open -= 1
                if open < 0:
                    break
                if k - j + 1 > maxi and open == 0:
                    maxi = k - j + 1
            j += 1
        return maxi

# finding longest valid parentheses in string

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxi = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    if i - stack[-1] > maxi:
                        maxi = i - stack[-1]
    return maxi

# fast stack solution
