class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        max_area = 0
        offsets = ((0,1), (0,-1), (1,0), (-1,0))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0: # water, skip
                    continue
                
                queue.append((i,j))
                grid[i][j] = 0 # visited
                area = 0
                while queue:
                    cur_i, cur_j = queue.popleft()
                    area += 1
                    for off_i, off_j in offsets:
                        if (not (0 <= (cur_i + off_i) < rows)) or (not (0 <= (cur_j + off_j) < cols)):
                            continue
                        
                        if grid[cur_i + off_i][cur_j + off_j] == 0:
                            continue
                        
                        queue.append((cur_i + off_i, cur_j + off_j))
                        grid[cur_i + off_i][cur_j + off_j] = 0 # mark water (visited)
                
                max_area = max(area, max_area)
                
        return max_area