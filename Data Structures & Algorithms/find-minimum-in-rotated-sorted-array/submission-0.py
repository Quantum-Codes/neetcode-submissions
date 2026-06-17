class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        """
        Possible:
        2 3 4 5 0 1
        6 0 1 2 3 4 5
        if:
            left < mid < right - left itself
            left > mid < right, Target is between left and mid
            left < mid > right, Target is between mid and right
        """
        while nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


