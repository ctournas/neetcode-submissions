class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                dayT, dayIdx = stack.pop()
                res[dayIdx] = i - dayIdx
            stack.append((t, i))
        return res
        