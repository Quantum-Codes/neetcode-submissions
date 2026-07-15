# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def checkGood(root, max_until_now):
            cur_good = 0
            if not root:
                return 0

            if (root.val >= max_until_now):
                cur_good = 1
            
            leftgood = rightgood = 0
            if root.left:
                leftgood = checkGood(root.left, max(root.val, max_until_now))
            if root.right:
                rightgood = checkGood(root.right, max(root.val, max_until_now))
            
            return leftgood + rightgood + cur_good
        
        return checkGood(root, -float('inf'))