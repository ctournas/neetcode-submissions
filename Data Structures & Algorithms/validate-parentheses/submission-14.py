class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {"}":"{", "]":"[",")":"("}
        stack = []

        for sym in s:
            if sym in symbols:
                if stack and symbols[sym] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sym)
        
        return True if not stack else False


        