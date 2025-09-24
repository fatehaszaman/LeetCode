# Leetcode question number 33
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Search right
                else:
                    right = mid - 1  # Search left

        return -1
