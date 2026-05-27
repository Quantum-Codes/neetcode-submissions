class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                width = j-i
                max_area = max(max_area, width*min((heights[i], heights[j])))
        
        return max_area