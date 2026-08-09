class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # edges in tree = n-1. here its n
        parent = [i for i in range(len(edges))]
        # off by 1 btw
        rank = [0] * len(edges)

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return True # found the cycle
            if rank[x] < rank[y]:
                parent[x] = y
            elif rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[y] = x
                rank[x] += 1
            
        for u, v in edges:
            u -= 1
            v -= 1
            if union(u, v):
                return [u+1, v+1]
        
        return []