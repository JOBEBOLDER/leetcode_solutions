# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # dfs traverse
    # time:On
    #space:On
    def __init__(self):
        self.res = []

    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.res

    def traverse(self,root:Optional[TreeNode]):
        if root is None:
            return


        if root and root.left is None and root.right is not None:
            self.res.append(root.right.val)
        
        if root and root.right is None and root.left is not None:
            self.res.append(root.left.val)

        self.traverse(root.left)
        self.traverse(root.right)
