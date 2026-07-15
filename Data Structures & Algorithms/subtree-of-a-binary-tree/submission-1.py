# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "#"
            # Wrap values to prevent false substring matches (e.g., ^12$ vs ^2$)
            return f"^{node.val}${serialize(node.left)}{serialize(node.right)}"
        
        # O(N + M) time and space
        return serialize(subRoot) in serialize(root)