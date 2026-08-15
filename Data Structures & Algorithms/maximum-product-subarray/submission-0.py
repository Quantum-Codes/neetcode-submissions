class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 2 pointer?
        # well but 2 negative numbers can increase the total product by a lot too
        # need to iterate through all
        # if i do a prefix product then: prod[i]/prod[j] = j+1...i product
        # if we put a -1th item "1" then prod[i]/prod[j] = j...i product
        # now even for division, if both negative then too possible for max
        # this preprocessing O(N) allows to compute products in O(1)
        # len = 2e4, so 4e8 = N^2. not allowed if 1e8 is limit. NlogN

        # need to make prod[i] max and prod[j] min, but not negative.
        # max prod can genuinely be negative? only when 1 element arr.
        # lets trace [2 4 -3 5]: [2 8 -24 -120]

        # there can be a 0 in between too that kills the preprocessing
        # rip. kill approach

        # state transition:
        # on each element, min can go to max and max can 
        # go to min. so track both.
        max_prod = min_prod = soln = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            max_prod, min_prod = max(n, n*max_prod, n*min_prod), min(n, n*max_prod, n*min_prod)
            soln = max(soln, max_prod)
        
        return soln
