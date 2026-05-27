class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Step 1: Sort the array (Takes O(N log N))
        soln = []
        n = len(nums)
        
        for i in range(n - 2):
            # If the current number is greater than 0, three positive numbers 
            # can never sum to 0. We can stop early!
            if nums[i] > 0:
                break
                
            # Clean Condition: Skip duplicate values for the anchor element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Two-pointer 2Sum on the remaining sorted portion
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    soln.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Clean Condition: Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Clean Condition: Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total < 0:
                    left += 1 # Sum too small, move left pointer right to increase sum
                else:
                    right -= 1 # Sum too big, move right pointer left to decrease sum
                    
        return soln