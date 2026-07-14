# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root) -> tuple[int, bool]:
            if root is None:
                return 0, True
            
            left, l_bal = getDepth(root.left)
            right, r_bal = getDepth(root.right)

            balanced = l_bal and r_bal and (abs(right-left) <= 1)
            return max(left+1, right+1), balanced
        
        return getDepth(root)[1]