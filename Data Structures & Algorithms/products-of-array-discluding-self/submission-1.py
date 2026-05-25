class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # each item i = prefix[i-1] * suffix[i+1]
        prefix = [nums[0]] # length min 2
        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i-1])
        
        out = [1] * len(nums)
        suffix = 1
        # we build output and calcualte suffix at same time
        for i in range(len(nums)-1, -1, -1):
            prefix_prod = 1 if i == 0 else prefix[i-1]
            out[i] = prefix_prod * suffix
            suffix *= nums[i]
        
        return out

