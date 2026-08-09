class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x] += 1
            
            return True
        
        for u, v in edges:
            if not union(u, v): # already connected
                return False
        
        parent = [find(i) for i in range(n)]
        if len(set(parent)) != 1:
            return False # disconnected
            
        return True