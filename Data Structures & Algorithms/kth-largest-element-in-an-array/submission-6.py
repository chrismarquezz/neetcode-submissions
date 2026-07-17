class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heap[0]