class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Brute: O(N*2^N) (2^N subsets and N for summing them up)
        # Minor optimization: DP table of binary of chosen/not chosen
        # Now sum itself is cached. So O(2^N) for all, not N per subsets
        # So O(2^N). still bad

        # since its partitioning, there need to be mutex elements
        # also the only possibility of it being same is if sum is half
        # so odd sum immediately gone. 
        # Problem converted to: "can we make a subset with sum(arr)/2"?
        # If sum is 0 then eeven nullset can achieve that.
        # We can theoretically start with random initialised bitstring:
        # if len(Arr)=4, then random bitstring=1011 meaning choose these elements 
        # or maybe we can try from 0000 or 1111
        # Now if sum > sum(Arr)/2 then:
        #   Try remove on each of the 1s. Cache this choice so later we dont 
        #   include it again in the same decision tree. On each choice we 
        #   eliminate half of the choices possible (of 2^N)
        #   After doing that, call this func again
        # if it was less then:
        #   Try including an item except for the exclusion list and thats 0
        #   Save this choice too since we wont touch this bit again too like the 
        #   first bit too. We have toggled and tried, no more changing.
        #   this also reduces it by 1/2.
        # if exactly equal then found solution, exit.
        # Depth of tree would be N. but paths travelled? not all surely?

        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = {0}
        for num in nums:
            next_dp = set()
            for s in dp:
                if s+num == target:
                    return True
                if s+num < target:
                    next_dp.add(s+num)
                next_dp.add(s)
            dp = next_dp
        
        return target in dp