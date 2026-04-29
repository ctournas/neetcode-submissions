class Solution:
    def isValid(self, s: str) -> bool:
        sym = {')':'(', '}':'{', ']': '['}
        stack = []
        if not s:
            return False

        for string in s:
            if string in sym:
                if stack and stack[-1] == sym[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)
        
        return True if not stack else False

        