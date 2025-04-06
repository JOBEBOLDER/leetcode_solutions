# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # use dfs, postorder can record the maxdepth
    # the reason why we are using postorder here because when we are calculateing curr node,
    #we need to know the left and right subtree depth first
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.max_diameter

    def traversal(self, root:Optional[TreeNode])->int:
        #base case:
        if root is None:
            return 0
        
        left = self.traversal(root.left)
        right = self.traversal(root.right)

        self.max_diameter = max(self.max_diameter, left + right)
        return 1 + max(left,right) #return 出去可以继续给之后调用计算