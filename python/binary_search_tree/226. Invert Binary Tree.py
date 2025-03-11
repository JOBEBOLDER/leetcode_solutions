# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #easy#binarysearch tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root

    def traverse(self, root:Optional[TreeNode]):
        #base case
        if root is None:
            return 

        tmp = root.right
        root.right = root.left
        root.left = tmp

        self.traverse(root.left)
        self.traverse(root.right)