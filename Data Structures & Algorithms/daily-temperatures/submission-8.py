class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            index = i
            while stack and stack[-1][1] < t:
                dayT, temp = stack.pop()
                index = i - dayT
                res[dayT] = index
            stack.append((i, t))
        return res
        