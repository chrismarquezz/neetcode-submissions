class Solution:
    def search(self, nums: List[int], target: int) -> int:
        halves = self.split_nums(nums)
        print(halves)
        for i in range(2):
            left = 0
            right = len(halves[i]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                print(mid)
                if halves[i][mid] > target:
                    right = mid - 1
                    print(right)
                elif halves[i][mid] < target:
                    left = mid + 1
                    print(left)
                else:
                    return mid if i == 0 else mid + len(halves[0])
        return -1

    def split_nums(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return [nums[0:left], nums[left:]]
