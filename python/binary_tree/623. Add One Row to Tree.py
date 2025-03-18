# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #time:On
    #space:Oh
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Special case when depth is 1
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        # Otherwise, use DFS with depth tracking
        self.dfs(root, val, depth, 1)
        return root
    
    def dfs(self, root: Optional[TreeNode], val: int, target_depth: int, current_depth: int):
        # Base case
        if root is None:
            return
        
        # If we're at the depth just above where we need to insert
        if current_depth == target_depth - 1:
            # Save original left and right children
            old_left = root.left
            old_right = root.right
            
            # Create new nodes with the value
            root.left = TreeNode(val)
            root.right = TreeNode(val)
            
            # Connect the original children to the new nodes
            root.left.left = old_left
            root.right.right = old_right
            return
        
        # Continue DFS
        self.dfs(root.left, val, target_depth, current_depth + 1)
        self.dfs(root.right, val, target_depth, current_depth + 1)


