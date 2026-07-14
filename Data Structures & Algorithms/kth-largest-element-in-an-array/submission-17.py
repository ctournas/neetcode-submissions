class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        l, r = 0, len(nums)-1

        while l <= r:
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if k > p:
                l = p + 1
            elif k < p:
                r = p - 1
            else:
                return nums[p]
        