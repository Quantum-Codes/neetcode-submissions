class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # We can make a graph, repeatedly trying to build prefix of the string
        # eg: [cats,cat] -> [in, sin] -> [car] -> x (dead, no prefix = s)
        # lets say s.len = N, wordDictlen = M, wordDict[i].len = P
        # N > M > P
        # For checking the next node of a node, it takes O(M) checks and each
        # takes O(P) time. So O(MP) to find next node for one node.
        # depth of tree d = N / min(P) along the way, max d = N
        # Root: (MP)
        # layer 1: (MP)*M
        # layer 2: (MP)*M*M
        # layer N-1: P*(M**N)
        # Sum: MP + M^2P + ... M^N P = MP(1+M+M^2+...+M^(N-1))
        # = MP(M^N-2)/M-1 == O(P*M^N) - naive BFS worst case

        # Subproblem: given index i in string s, is it possible to fill 0...i
        # of the string such that 0...i matches the string's 0...i
        # dp[i] = any(dp[0...i-1 (call index j)] and E s[j+1:i+1] == word)
        # But then to fill every dp[i], we need a O(N) over dp arr, then
        # a O(MP) scan over each word at each dp[i] during the scan.
        # So for each dp[i], we need a O(NMP) scan.
        # So total = O(MP*N**2) == 4e4 * 2e3 = 8e7 allowed (barely?)

        words = set(wordDict)
        dp = [False] * len(s)
        for i in range(0, len(s)):
            for j in range(0, i):
                if dp[j] == False:
                    continue
                if dp[i] == True: # microoptimization, break early
                    break
                # find appropriate word
                if s[j+1:i+1] in words:
                    dp[i] = True
                    continue
            
            # finally also check if theres a word that can fill 0...i entirely:
            # we could also put this in the loop itself but eh..
            # For that make subprobelm be to fill 0..i-1 so dp[0] means fill nothing and thats always true
            # and then make another item dp[N] to return 
            if dp[i] == False:
                if s[0:i+1] in words:
                    dp[i] = True
        
        return dp[-1]
                