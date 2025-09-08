class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rs = s[::-1]
        for i in range(1, len(s)):
            curr = s[i-1] + s[i]
            if curr in rs:
                return True
        return False

# find if String of lenght 2 in reverse exists in same String
