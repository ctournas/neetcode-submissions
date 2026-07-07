class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) >= 2:
            x, y = stones.pop(), stones.pop()
            total = x - y
            if total > 0:
                stones.append(total)
                stones.sort()
        return stones[0] if stones else 0