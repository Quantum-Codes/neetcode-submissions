class Solution:
    #modifies the arr. soln2 for not doing that
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            # Use the absolute value because the number might have been 
            # negated by a previous visit
            index = abs(nums[i]) - 1
            
            # If the value at this index is negative, we've seen it before
            if nums[index] < 0:
                return abs(nums[i])
            
            # Otherwise, mark it as seen by negating it
            nums[index] = -nums[index]
        
        return -1