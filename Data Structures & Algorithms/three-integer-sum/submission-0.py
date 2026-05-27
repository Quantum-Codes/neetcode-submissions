class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # reducing 3 sum into 2 sum -> target = target - nums[i]
        # n becomes n^2
        target = 0
        soln = []
        for reduce_target in range(len(nums)):
            # inside here solve 2sum
            vals = {}
            for i in range(len(nums)):
                vals[target - nums[reduce_target] - nums[i]] = i
            for i in range(len(nums)):
                if vals.get(nums[i]) is not None and i != vals[nums[i]] != reduce_target != i:
                    soln.append(tuple(sorted((nums[reduce_target], nums[i], nums[vals[nums[i]]]))))
            

        return list(set(soln))

