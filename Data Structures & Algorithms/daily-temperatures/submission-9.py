class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                dayT, temp = stack.pop()
                res[dayT] = i - dayT
            stack.append((i, t))
        return res
        