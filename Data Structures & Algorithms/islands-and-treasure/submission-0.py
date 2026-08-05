class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # could start out from every treasure chest and mark every neighbor
        # as the min(cur_val, distance_current) and the moment we encounter
        # another chest as neighbor, we stop traversing that cell and any 
        # neighbors of that cell added to the queue is removed
        # need to maintain a separate visited queue to check if current 
        # treasurechest traversal doesnt go back. but cleared when starting
        # another chest. Unreachable is inf anyway so no need special case.
        # this is O(m*n * m*n) maybe. Not exactly but good upper bound?
        # complexity allowed acc to constraints (m,n<=100) but too close

        # also could try finding distances from the topleft and treat
        # chests as pass-through so we dont have fake unreachable areas
        # eh wont work cuz then need to go back to the chests and reverse
        # distances by a <chest distance> - <cell from topleft> - const 
        # something like this. again can be O(m*n * m*n)

        # oh we can just start a BFS from all chests and never visit again
        # due to BFS properties the existing value will be optimal
        # O(m*n)
        # distance from chest is 0 so no special there too
        
        rows = len(grid)
        cols = len(grid[0])
        offsets = ((1,0), (-1,0), (0,1), (0,-1))

        queue = deque()
        # enqueue all the chests
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j)) # cell val already 0

        # Visited: value != INF
        # we never add water

        # start multisource BFS
        while queue:
            i, j = queue.popleft()
            
            for off_i, off_j in offsets:
                if not (0 <= i+off_i < rows) or not (0 <= j+off_j < cols):
                    continue
                if grid[i+off_i][j+off_j] != 2**31 - 1:
                    continue
                
                grid[i+off_i][j+off_j] = grid[i][j] + 1
                queue.append((i+off_i, j+off_j))

            



