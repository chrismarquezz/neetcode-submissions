class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        max_seq = 0
        curr_seq = 0
        for n in nums:
            curr_num = n
            if curr_num - 1 not in nums_set:
                curr_seq = 1
                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_seq += 1
                max_seq = max(max_seq, curr_seq)
        return max_seq