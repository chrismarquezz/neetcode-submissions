class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        result = []

        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in counts.items():
            buckets[val].append(key)

        for i in range(len(buckets) - 1 , -1, -1):
            if len(result) < k:
                for num in buckets[i]:
                    result.append(num)

        return result
