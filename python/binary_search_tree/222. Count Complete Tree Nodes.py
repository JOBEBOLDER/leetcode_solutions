# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #因为题目说的是1-n个节点，所以可以直接赋值给left+right，然后加上root本身，
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        return self.traverse(root)

    def traverse(self, root:Optional[TreeNode]):
        if root is None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        treeNum = left + right + 1

        return treeNum



        