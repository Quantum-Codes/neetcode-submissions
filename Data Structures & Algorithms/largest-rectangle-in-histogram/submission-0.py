class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_smaller_element = [-1] * len(heights)
        next_smaller_element = [len(heights)] * len(heights) # init all to beyond last element

        # next smaller
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                next_smaller_element[stack.pop()] = i
            stack.append(i)
        
        # prev smaller
        stack.clear()
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                prev_smaller_element[stack.pop()] = i
            stack.append(i)
        
        area = 0
        for i in range(len(heights)):
            area = max(area, (next_smaller_element[i] - prev_smaller_element[i] - 1) * heights[i])
        
        return area