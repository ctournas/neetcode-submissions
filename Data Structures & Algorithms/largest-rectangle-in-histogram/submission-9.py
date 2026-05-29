class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxRec = 0
        for i, h in enumerate(heights):
            start = i
            while stack and  stack[-1][1] > h:
                index, height = stack.pop()
                maxRec = max(maxRec, height*(i-index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxRec = max(maxRec, h*(len(heights)- i))
        return maxRec
        