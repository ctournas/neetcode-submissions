class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first, second = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            des = first - second
            if des:
                heapq.heappush(maxHeap, des)
        return abs(maxHeap[0]) if maxHeap else 0
        