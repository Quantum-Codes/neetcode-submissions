class Solution:
    def numDecodings(self, s: str) -> int:
        # s = "1234567890"
        # start with individuals. oh but 0 comes too.
        # basically need to find all groupings possible: max 2 digit
        # and then later subtract with all the improper ones
        # need a mix of 1 and 2 groups at all times tho
        # so we choose how many 1 groups and then calculate?
        # out of n chars we choose x chars as 1 groups, n-x make 2 groups
        # oh but its possible now that 1 gap creates yet another 1 groupings
        # better choose how many 2 groups need to exist
        # there can be n-1 of 2 groups total. n-1Cx chosen groups. but there
        # is overlap of chars that we dont want. once we choose one group then 
        # those 2 elements need to be gone. Choose from permutations cant do it
        # Initially we had n-1. then we choose 1, then we have a conditional num
        # of other groups possible. eh this is hard.

        # what if divide and conquer? oh dp i can see roughly
        # i...j how many possibilities is the subproblem
        # what about 0...i? 
        # "1" -> 1
        # "11" -> 2
        # "111" -> 3
        # "1111" -> 5
        # oh so its basically dp[i] = dp[i-1] + (s[i]>0) + (s[i-1]>0 and 0<s[i-1:i+1]<27)
        # but its not ways. we need to extend the existing ways
        # so if double is valid, i-1 char must not be in a single. so use i-2
        # if single is valid then it extends the i-1 number of ways
        # oh so if i append 0 then its possible that ways go to zero??
        # "19" -> has 2 ways.
        # appending "0": "190". 2 not valid, 1 not valid. ways= oh 0?? wow

        if s[0] == "0":
            return 0

        dp = [1] * len(s)
        for i in range(1, len(s)):
            dp[i] = dp[i-1] * (int(s[i])>0) + dp[i-2] * (int(s[i-1])>0 and 0<int(s[i-1:i+1])<27)
        
        return dp[-1]
            