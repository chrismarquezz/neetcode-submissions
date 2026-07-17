class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in counts.items():
            buckets[val].append(key)
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(res) < k:
                    res.append(num)
        return res