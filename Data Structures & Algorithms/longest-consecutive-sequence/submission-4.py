class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                current = n
                while (current + 1) in num_set:
                    length += 1
                    current += 1

                max_length = max(max_length, length)

        return max_length