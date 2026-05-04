class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDict = {']': '[', ')': '(', '}': '{'}

        for sym in s:
            if sym in myDict:
                if stack and stack[-1] == myDict[sym]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sym)
        
        return True if not stack else False
        

        