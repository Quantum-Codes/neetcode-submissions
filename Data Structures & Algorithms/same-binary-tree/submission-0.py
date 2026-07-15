# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) ^ (q is None):
            return False
        elif p is not None:
            leftSame = self.isSameTree(p.left, q.left)
            rightSame = self.isSameTree(p.right, q.right)
            return leftSame and rightSame and p.val == q.val
        else:
            return True


        return False