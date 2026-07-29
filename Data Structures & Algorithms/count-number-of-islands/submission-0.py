class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [False] * (rows * cols) # store visited land. water is ignored anyway

        island_count = 0
        for cell_id in range(rows * cols): # makes sure we scan every cell
            if visited[cell_id]: # for not repeating scan from inner BFS
                continue
            
            cell_row = cell_id // cols
            cell_col = cell_id % cols

            if grid[cell_row][cell_col] == "0":
                continue

            # scan current island
            island_count += 1
            queue = deque([cell_id])
            visited[cell_id] = True
            while queue:
                cur_cell = queue.popleft()
                i = cur_cell // cols
                j = cur_cell % cols

                for i_off, j_off in [(1,0), (-1, 0), (0,1), (0,-1)]:
                    if not (0 <= i+i_off < rows) or not (0 <= j+j_off < cols):
                        continue # off bounds
                    new_cell_id = (i+i_off)*cols + (j+j_off)
                    if grid[i+i_off][j+j_off] == "0" or visited[new_cell_id]:
                        continue # water
                    
                    # now we knoe its land. add to queue
                    queue.append(new_cell_id)
                    visited[new_cell_id] = True
                
        return island_count