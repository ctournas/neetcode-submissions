class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-s for s in nums]
        heapq.heapify(minHeap)
        while k > 0:
            res = heapq.heappop(minHeap)
            k -= 1
            if k == 0:
                return -res 
        