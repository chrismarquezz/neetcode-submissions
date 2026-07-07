class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        heap = list(counts.keys())
        heapq.heapify(heap)
        if len(hand) % groupSize != 0:
            return False
        while heap:
            card = heapq.heappop(heap)
            if counts[card] > 0:
                for i in range(groupSize):
                    v = card + i
                    if counts[v] <= 0:
                        return False
                    counts[v] -= 1
                heapq.heappush(heap, card)
        return True