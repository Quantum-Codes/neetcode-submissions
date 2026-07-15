# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        soln = []
        while queue:
            cur, level = queue.popleft()
            if len(soln) == level:
                soln.append([])
            
            soln[level].append(cur.val)
            if cur.left:
                queue.append((cur.left, level+1))
            if cur.right:
                queue.append((cur.right, level+1))
            
        return soln