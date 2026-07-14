# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depthOfTree(root, diameter):
            if root is None:
                return 0, 0
            
            left, d_left = depthOfTree(root.left, diameter)
            right, d_right = depthOfTree(root.right, diameter)

            diameter = max(d_left, d_right, left + right)
            
            return max(left + 1, right + 1), diameter
        
        depth, diameter = depthOfTree(root, 0)
        return diameter
        