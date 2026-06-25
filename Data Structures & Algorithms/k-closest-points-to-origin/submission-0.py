class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = points
        res = []
        for i in range(len(points)):
            points[i] = (math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2), points[i])
        for _ in range(k):
            heapq.heapify(heap)
            point = heapq.heappop(heap)
            res.append(point[1])
        return res