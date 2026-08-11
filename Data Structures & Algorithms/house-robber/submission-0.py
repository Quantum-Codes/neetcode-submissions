class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = optimal robbing 0...i house
        # dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        # again only need 3 items. 
        # its 3 so again vars. else would do deque
        # answer is max(dp[-1], dp[-2])

        # lets do a standard dp first
        # not modifying nums arr, else would be O(1)
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            back2 = dp[i-2] if i >= 2 else 0
            back3 = dp[i-3] if i >= 3 else 0

            dp[i] = max(back2, back3) + nums[i]

        return max(dp[-1], dp[-2])