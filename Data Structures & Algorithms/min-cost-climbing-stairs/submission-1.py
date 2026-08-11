class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = dp[i] (cost) + min(dp[i-1],dp[i-2])
        # we are only using last 2 vals, 
        # dont need full arr.
        # dp[i] = to reach and stand on i

        cost.append(0) # stand on last = 0
        one_back, two_back = cost[1], cost[0]
        
        for i in range(2, len(cost)):
            one_back, two_back = min(one_back, two_back) + cost[i], one_back
        
        return one_back
        