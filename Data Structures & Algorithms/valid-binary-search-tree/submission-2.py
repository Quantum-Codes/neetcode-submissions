# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root, leftbound, rightbound):
            if root is None:
                return True
            
            if not leftbound < root.val < rightbound:
                return False
            
            leftvalid = isvalid(root.left, leftbound, root.val)
            rightvalid = isvalid(root.right, root.val, rightbound)
        
            return leftvalid and rightvalid
        
        return isvalid(root, -float('inf'), float('inf'))
