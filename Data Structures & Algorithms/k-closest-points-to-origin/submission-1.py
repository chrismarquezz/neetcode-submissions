class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i in range(len(points)):
            heapq.heappush(heap, (((points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2), (points[i][0], points[i][1])))
        for _ in range(k):
            point = heapq.heappop(heap)
            res.append(point[1])
        return res