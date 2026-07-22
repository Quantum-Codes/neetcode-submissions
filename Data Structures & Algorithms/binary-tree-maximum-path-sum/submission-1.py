# Definition for a binary tree node.
# class TreeNode:
from types import MappingProxyType
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_found = -float('inf')

        def sumpath(root) -> int:
            nonlocal max_found
            if root is None:
                return 0 # branch_max
            
            left_branch = sumpath(root.left)
            right_branch = sumpath(root.right)
            branch_sum = max(left_branch, right_branch, 0) + root.val
            max_found = max(max_found, branch_sum, left_branch+right_branch+root.val, root.val)
            return branch_sum

        sumpath(root)
        return max_found
        
