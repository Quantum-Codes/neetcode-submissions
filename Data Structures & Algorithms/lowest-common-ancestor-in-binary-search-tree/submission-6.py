# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #   APPROACH TO LCA ON GENERAL TREES (with bitmasking genius)
        self.lca = None
        def find2nodes(root, p: int, q: int) -> int: # 2bits
            if root is None:
                return 0
            
            foundinleft = find2nodes(root.left, p, q)
            foundinright = find2nodes(root.right, p, q)

            foundhere = foundinright | foundinleft | (root.val == p) << 1 | (root.val == q)
            if foundhere == 0b11 and self.lca is None:
                self.lca = root
            
            return foundhere
        
        find2nodes(root, p.val, q.val)
        return self.lca