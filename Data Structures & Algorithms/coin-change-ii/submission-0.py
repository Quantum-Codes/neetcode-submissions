class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # combinations..
        # so for the standard bfs tree i need to remove
        # the duplicate permuted branches and persist one
        # lets say i choose coins in descending order
        # ie if coins are 2 1 4 5 3 then i choose as
        # 5 4 3 2 1 always
        # how to do that though?
        # ah lets try brute again. i should start with it
        # [1 2 3], 4. lets say: how many to get 4 with [1]
        # 1 way. that only if 4 % coin == 0
        # then how to get 4 with [1 2]
        # that would be dp[1] + (4%2==0) + mix??
        # mix will already be a part of dp[1]
        # oh but 4%1 will also be a part
        # need some kind of bool flag counting?
        # dp[1] * (condition to extend) + new ways
        # dp[i] = dp[i-c1]*(1) + dp[i-c2] + ...
        # has to be this. standard addition wihtout bool
        # now need to enforce the ordering
        # is dupe branching even a problem now that we are
        # extending existing combinations? doesnt seem so
        # yeah we arent. or wait.. maybe we are?
        # lets say it took:
        #   18 = [ 5 5 8 ]
        #   10 = [5 5]
        #   13 = [8 5]
        #   18 = (10)+8 and (13)+5
        # yes there is double counting

        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i-c]
        
        return dp[amount]