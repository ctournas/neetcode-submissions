class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {"]":"[", "}":"{", ")":"("}
        stack = []

        for sym in s:
            if sym in symbols:
                if stack and stack[-1] == symbols[sym]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(sym)
        
        return True if not stack else False
        