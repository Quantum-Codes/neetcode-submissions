class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # greedy? [2 3 10], 14 -> 3 coins kinda. greedy didnt work. lets say we backtrack at choosing 3 and go to choose 2. now its greedy+dfs.
        # [1 3 4], 6 -> here even that doesnt work.
        # bruteforce would be to just explore every coin 
        # choosing path and get min depth (bfs until 0)
        # DP would be ???. cant think. lemme draw bfs to see
        # okay many branches seem the same.
        # so subproblem is that given a amount x, find 
        # minimum to get to that x.
        # then dp[i] = min(dp[x] : x=i-c for all c)

        dp = [0] * (amount+1) # O(amount*coins.len)? worse than bfs?
        # dp[0] = 0
        for i in range(1, amount+1):
            min_coins = float('inf')
            for c in coins:
                if i-c < 0:
                    continue
                min_coins = min(min_coins, dp[i-c])

            dp[i] = min_coins + 1
        
        return dp[amount] if dp[amount] != float('inf') else -1
