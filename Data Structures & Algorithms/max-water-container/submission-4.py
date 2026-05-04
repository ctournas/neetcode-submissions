class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            if heights[l] > heights[r]:
                area = min(heights[l], heights[r]) * (r-l)
                res = max(res, area)
                r -= 1
            else:
                area = min(heights[l], heights[r]) * (r-l)
                res = max(res, area)
                l += 1
        return res
