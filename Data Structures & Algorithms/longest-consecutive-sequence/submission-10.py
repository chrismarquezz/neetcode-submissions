class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0
        for n in num_set:
            curr_num = n
            temp_seq = 1
            if n - 1 not in num_set: 
                while curr_num + 1 in num_set:
                    curr_num += 1
                    temp_seq += 1
            max_seq = max(max_seq, temp_seq)
        return max_seq