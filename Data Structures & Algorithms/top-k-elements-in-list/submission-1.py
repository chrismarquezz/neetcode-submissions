class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []
        buckets = [[] for num in range(len(nums) + 1)]
        print(counts)
        print(buckets)
        for key, val in counts.items():
            buckets[val].append(key)

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(res) < k:
                    res.append(num)

        return res
