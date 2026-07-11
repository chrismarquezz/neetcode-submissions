class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in counts.items():
            buckets[val].append(key)
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                if len(res) < k:
                    res.append(n)
        return res
    