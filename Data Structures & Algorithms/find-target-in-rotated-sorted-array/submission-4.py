class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        """
        IF left arr sorted AND contains target:
            right = mid # mid itself can be target
        IF left arr sorted AND NOT contains target:
            left = mid + 1
        IF right arr sorted AND contains target:
            left = mid
        IF right arr sorted AND NOT contains target:
            right = mid - 1
        """
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
                
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        
        return -1
            