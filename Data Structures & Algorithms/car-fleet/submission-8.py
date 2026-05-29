class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cords = [(p,s) for p, s in zip(position, speed)]
        cords.sort(reverse=True)
        stack = []

        for p, s in cords:
            time = ((target-p)/s)
            stack.append(time)
            if len(stack)>1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)