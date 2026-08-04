"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodemap = {}
        new_node = Node(node.val)
        nodemap[node] = new_node

        queue = deque([node])
        while queue:
            cur = queue.popleft()

            if cur.neighbors == []: 
                continue
            
            for item in cur.neighbors:
                if item not in nodemap:
                    queue.append(item)
                    nodemap[item] = Node(item.val)
                nodemap[cur].neighbors.append(nodemap[item])
        
        return new_node