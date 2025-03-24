# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #medium
    #time:On
    #space:Oh
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse(root)
        return root
        
        
    def traverse(self, root:Optional[TreeNode]):
        #base case:
        if root is None:
            return

        #cuz the order shown in the pic that the result is decreasing order
        #we need to traverse the right subtree then left base on the idintities of the BST

        self.traverse(root.right)
        #keep track of the sum of the tree
        self.sum += root.val

        root.val = self.sum

        self.traverse(root.left)
