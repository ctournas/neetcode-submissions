class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = {')': '(', ']': '[', '}': '{'}

        for sym in s:
            if sym in closetoOpen:
                if stack and stack[-1] == closetoOpen[sym]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sym)

        return True if not stack else False            
        