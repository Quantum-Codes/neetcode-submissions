class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for item in nums:
            product *= item if item != 0 else 1
        
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        if nums.count(0) == 1:
            out =  [0] * len(nums)
            out[nums.index(0)] = product
            return out
        
        return [int(product/item) for item in nums]
