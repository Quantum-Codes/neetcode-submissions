class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        # nums[left] is the minimum now
        if target > nums[-1]:
            #then its in the left subarr. binarysearch(0, left)
            right = left
            left = 0
        else:
            # then in right subarr. binary search(left, end)
            right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1