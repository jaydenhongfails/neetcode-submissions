class Solution:
    def isValid(self, s: str) -> bool:
        res = {"(": ")", "{": "}", "[": "]"}
        stack = []


        for k in s:
            if k in res:
                stack.append(k)
            else:
                if not stack:
                    return False 
                top = stack.pop()
                if res[top] != k:
                    return False
        
        return len(stack) == 0