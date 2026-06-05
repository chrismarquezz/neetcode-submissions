class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        heap = []

        for key, val in counts.items():
            heapq.heappush_max(heap, (val, key))
        
        for i in range(k):
            element = heapq.heappop_max(heap)
            res.append(element[1])
        
        return res