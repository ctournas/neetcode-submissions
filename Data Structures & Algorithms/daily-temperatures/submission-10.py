class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for day, t in enumerate(temperatures):
            while  stack and t > stack[-1][1]:
                dayT, temp = stack.pop()
                res[dayT] = day - dayT
            stack.append((day, t))
        return res