# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(root, minval, maxval):
            if not root:
                return True
            
            if not (minval < root.val < maxval):
                return False
                
            return checkValid(root.left, minval, root.val) and checkValid(root.right, root.val, maxval)
        

        return checkValid(root, -float('inf'), float('inf'))