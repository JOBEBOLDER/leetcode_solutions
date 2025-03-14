# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BST: set two variable,one is minnode, maxnode, and iterative these node ,compare all of the nodes with these two variable
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, None, None)

    def valid(self, root: Optional[TreeNode], min_node:Optional[TreeNode], max_node:Optional[TreeNode]):
        #base case
        if root is None:
            return True
        #判断的条件

        if min_node is not None and root.val <= min_node.val:
            return False

        if max_node is not None and root.val >= max_node.val:
            return False
        #recuresively return the result
        # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
        return self.valid(root.left, min_node, root) and self.valid(root.right, root, max_node)

       
        

    
    