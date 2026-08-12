class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def linear(start, end):
            back1, back2 = nums[start], 0
            for i in range(start+1, end):
                back1, back2 = max(back2+nums[i], back1), back1
            return back1

        
        return max(linear(0, len(nums)-1), linear(1, len(nums)))