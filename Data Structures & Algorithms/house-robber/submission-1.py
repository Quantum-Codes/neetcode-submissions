class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = optimal robbing 0...i house
        # dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        # again only need 3 items. 
        # its 3 so again vars. else would do deque
        # answer is max(dp[-1], dp[-2])

        b1, b2, b3 = nums[0], 0, 0
        for i in range(1, len(nums)):
            b1, b2, b3 = nums[i] + max(b2, b3), b1, b2

        return max(b1, b2)