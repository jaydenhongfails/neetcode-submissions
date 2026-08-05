class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"(":")", "[":"]", "{":"}"}

        for char in s:
            if char in pair:
                stack.append(char)
            elif not stack or pair[stack[-1]] != char:
                return False
            else:
                stack.pop()
            
        return not stack