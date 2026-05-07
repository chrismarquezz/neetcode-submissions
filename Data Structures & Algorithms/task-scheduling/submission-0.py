class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        pq = list(counts.values())
        heapq.heapify_max(pq)
        queue = deque()
        time = 0

        while pq or queue:
            time += 1
            if pq:
                count = heapq.heappop_max(pq) - 1
                if count > 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush_max(pq, queue.popleft()[0])

        return time
