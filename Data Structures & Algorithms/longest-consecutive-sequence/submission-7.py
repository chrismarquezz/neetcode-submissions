class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0

        for i in range(len(nums)):
            curr_num = nums[i]
            temp_seq = 1
            while curr_num + 1 in nums:
                curr_num += 1
                temp_seq += 1
            max_seq = max(max_seq, temp_seq)
        return max_seq