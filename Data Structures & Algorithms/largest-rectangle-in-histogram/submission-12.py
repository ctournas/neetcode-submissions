class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                res = max(res, height*(i-idx))

                start = idx
            stack.append((start, heights[i]))

        for idx, height in stack:
            res = max(res, height*(len(heights) - idx))

        return res
            

        