class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        res = []
        for x, y in points:
            p = x**2 + y**2
            heapq.heappush(minHeap, [p, x, y])
        
        while k > 0:
            p, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
        