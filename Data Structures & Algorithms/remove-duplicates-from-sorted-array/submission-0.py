class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        count = 1

        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                count += 1
                slow += 1
                nums[slow] = nums[fast]

        return count