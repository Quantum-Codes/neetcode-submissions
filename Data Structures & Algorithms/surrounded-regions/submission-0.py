class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # we start out by a dfs on every edge node thats O.
        # we mark every region with an edge.
        # Then we do a full traverse M*N and replace all Os thats 
        # not marked.
        # O(N*M)

        rows = len(board)
        cols = len(board[0])

        marked = set()
        def dfs(i, j):
            if not (0 <= i < rows and 0 <= j < cols):
                return
            if board[i][j] == "X":
                return
            if (i, j) in marked:
                return
            
            marked.add((i, j))
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        
        for j in range(cols):
            dfs(0, j)
            dfs(rows - 1, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in marked:
                    board[i][j] = "X"
        
        