# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def findDepth(root):
            if not root:
                return 0
            leftDepth = findDepth(root.left)
            rightDepth = findDepth(root.right)
            diameter = leftDepth + rightDepth
            self.maxDiameter = max(self.maxDiameter, diameter)
            return 1 + max(leftDepth, rightDepth)
        
        findDepth(root)
        return self.maxDiameter