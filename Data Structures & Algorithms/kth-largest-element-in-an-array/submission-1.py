class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        target = len(nums) - k
    
        while left <= right:
            pivot = (left+right)//2 # CHANGE
            p = left
            # keep pivot at end to avoid shifting elements
            nums[pivot], nums[right] = nums[right], nums[pivot]

            # now quickselect
            for i in range(left, right):
                if nums[i] <= nums[right]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            #now keep the pivot in the correct index p
            nums[p], nums[right] = nums[right], nums[p]

            # now check which half do we lie and continue iteration
            if target == p:
                return nums[p]
            elif target > p: # right part
                left = p + 1
            else:
                right = p - 1
                