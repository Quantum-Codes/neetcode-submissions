class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # O((NM)^2) allowed. need a O(M*N) seemingly
        # Could do a DFS - it explores one path at a time and when
        # changing branch only the last few nodes change.
        # we can maintain a global stack for the DFS that has the current
        # explored path and the moment we see its monotonically decreasing
        # for any subarr AND well.. for that we can track whether we
        # touched both waters?? umm idk how

        # actually a multisource BFS from all the edge nodes. They anyway
        # have info which water they touch. keep updaing state of every
        # node encountered.
        # We only expand if height of neighbor >= cur
        # effectively need a level-order multibfs traversal.
        # but we should be able to visit again for marking both as water
        # this failed too

        #obs:
        # top right and bottom left always reachable
        # If a neighbor of accepted cell is of higher height then its also
        # reachable form both oceans. Can we propogate a BFS from these?
        # all reachable land seems connected. actually no (found counter)

        # okay idea 2 was right, just had to run for both ocean 
        # separately so no need to visite agaiin
        atlantic, pacific = set(), set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(i, j, prev_val, visited):
            if (i,j) in visited:
                return 
            if not (0 <= i < rows and 0 <= j < cols):
                return
            if prev_val > heights[i][j]:
                return

            visited.add((i, j))
            dfs(i+1, j, heights[i][j], visited)
            dfs(i-1, j, heights[i][j], visited)
            dfs(i, j+1, heights[i][j], visited)
            dfs(i, j-1, heights[i][j], visited)

        for i in range(rows):
            dfs(i, 0, 0, pacific)
            dfs(i, cols - 1, 0, atlantic)
        
        for j in range(cols):
            dfs(0, j, 0, pacific)
            dfs(rows - 1, j, 0, atlantic)
        
        soln = atlantic & pacific
        return [[i, j] for i, j in soln]
