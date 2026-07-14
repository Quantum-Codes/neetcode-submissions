# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def switch(root):
            if root is None:
                return
            leftsubtree = root.left
            root.left = root.right
            root.right = leftsubtree
            
            switch(root.left)
            switch(root.right)
        
        switch(root)
        return root