class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            if x != y:
                heapq.heappush_max(heap, abs(y - x))
        return heap[0] if heap else 0