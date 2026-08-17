class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # subproblem: LIS until index i = dp[i]
        # each dp[i] stores how many numbers are < nums[i] in subsequence
        # each dp[i] loops back to see the max dp[i] with lesser val
        # dp[i] = max(dp[j] where nums[j] < nums[i] for 0<=j<i)
        # O(N^2)
        # the bruteforce would be - starting from every i, 
        # find the length of subsequence, and then max that over all i.
        # O(N^2)

        # does it need to be 0<=j? or can it just choose to not scan
        # it has to..
        # well lets change subproblem after seeing bruteforce
        # oh nvm im dumb. bruteforce complexity is wrong. even that uses dp
        # bruteforce is for every i, need to find next j and then continue
        # picking. at every i, i need to pick a j out of O(N) and again..
        # thats like N**N? idk how to do this complexity wtf?

        dp = [-1] * len(nums) 
        soln = 1
        dp[0] = 1 # itself
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]) # pick max dp[j]
            dp[i] = max(dp[i], 0) + 1 # itself or continue
            soln = max(soln, dp[i])
        return soln


        