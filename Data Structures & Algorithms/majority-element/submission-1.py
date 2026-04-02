class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        max_element = max(hashmap.values())

        for key, val in hashmap.items():
            if val == max_element:
                return key