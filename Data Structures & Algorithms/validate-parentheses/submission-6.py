class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        stack = []

        for sym in s:
            if sym in closeToOpen:
                if stack and stack[-1] == closeToOpen[sym]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sym)
        
        return True if not stack else False
        