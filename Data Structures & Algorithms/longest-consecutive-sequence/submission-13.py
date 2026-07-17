class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0
        curr_seq = 0
        for n in num_set:
            if n - 1 not in num_set:
                curr_seq = 1
                curr_num = n
                while curr_num + 1 in num_set:
                    curr_seq += 1
                    curr_num += 1
            max_seq = max(max_seq, curr_seq)
        return max_seq