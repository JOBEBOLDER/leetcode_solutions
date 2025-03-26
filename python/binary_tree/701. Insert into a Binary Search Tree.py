# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # input:root,given value
    # ouput:unque value
    #  BST :
    # preorder ->


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.preorder(root, val)
        

    def preorder(self,root:Optional[TreeNode],val:int):
        # base case:
        if root is None:
            return TreeNode(val)

        if val < root.val:
             # 递归调用，将返回值赋给右子节点
            root.left = self.preorder(root.left,val)
        else:
            root.right = self.preorder(root.right, val)

        return root

'''
T: O(H) 而不是 O(N)
# H是树的高度
# 原因：在BST中插入值时，我们不需要访问所有节点
# 而是沿着一条路径一直走到叶子节点
# - 在平衡BST中，H = log N
# - 在最坏情况（完全不平衡的BST），H = N

Space:
O(h)

'''

        