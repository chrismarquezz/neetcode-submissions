class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        count = 0

        while left <= right:

            if nums[left] != val:
                left += 1
            else:   
                count += 1
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        return len(nums) - count

            