class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res = [0]*len(temperatures)

        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx, temperature = stack.pop()
                res[idx] = day - idx
            stack.append((day, temp))
        return res
        