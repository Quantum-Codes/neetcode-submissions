# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def getDepth(root):
            if root is None or not self.balanced:
                return 0
            
            left = getDepth(root.left)
            right = getDepth(root.right)
            if self.balanced: # if we dont put this and rely on the top one before we make the calls then a lower node could edit the var and the var will be different from when it was tested. RACE CONDITION??
                self.balanced = abs(left - right) <= 1
            return 1 + max(left, right)
        
        getDepth(root)
        return self.balanced