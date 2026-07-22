# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded = ""
        def dfs(root):
            nonlocal encoded
            encoded += "," + (str(root.val) if root else "N")
            if root is None:
                return
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return encoded[1:]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = [int(item) if item.isdigit() else item for item in data.split(",")]
        queue = deque(preorder)

        def build_tree():
            if not queue:
                return None
            
            rootval = queue.popleft()
            if rootval == "N":
                return None
            root = TreeNode(val=rootval)
            root.left = build_tree()
            root.right = build_tree()
            return root
        
        return build_tree()