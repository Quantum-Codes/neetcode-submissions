class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        right = 0
        while right < len(height):
            item = height[right]
            right_wall = (right, item) # package similar to left
            if not stack or item <= stack[-1][1]:
                stack.append((right, item))
                right += 1
                continue
            else:
                base = stack.pop()[1]
                if not stack:
                    continue
                left_wall = stack[-1]
                # right wall is item
                water += (right_wall[0] - left_wall[0] - 1) * (min(left_wall[1], item) - base)

        return water
