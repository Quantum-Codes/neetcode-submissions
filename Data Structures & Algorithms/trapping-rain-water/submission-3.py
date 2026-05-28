class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        water = 0
        max_container_height = 0
        while left < right - 1:
            cur_height = min(height[left], height[right])
            if cur_height > max_container_height:  
                water += (right - left - 1) * (cur_height - max_container_height) # fill extra unfilled water
                max_container_height = cur_height
            
            if height[left] <= height[right]:
                left += 1
                water -= min(height[left], max_container_height)
            else:
                right -= 1
                water -= min(height[right], max_container_height)


        
        return water

