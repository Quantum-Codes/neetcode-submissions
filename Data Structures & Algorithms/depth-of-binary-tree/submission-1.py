# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [(root, 0)]
        soln = 0
        while stack:
            cur, d = stack.pop()
            if cur.left:
                stack.append((cur.left, d+1))
            if cur.right:
                stack.append((cur.right, d+1))

            if not (cur.left or cur.right): # meaning leaf
                soln = max(d+1, soln)

        return soln
                    