# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def checkGood(root, maxuntilnow):
            if root is None:
                return 
            
            self.good += 1 if maxuntilnow <= root.val else 0
            maxuntilnow = max(maxuntilnow, root.val)
            checkGood(root.left, maxuntilnow)
            checkGood(root.right, maxuntilnow)
        
        checkGood(root, -float('inf'))
        return self.good