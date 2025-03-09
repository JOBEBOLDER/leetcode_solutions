# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #time: On,n is the number of the tree node
    #space: OH, the height of the tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case
        if root is None or root == p or root == q:
            return root
            
        # 递归搜索左右子树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 处理结果
        if left and right:
            return root  # p和q分别在左右子树中，当前节点就是LCA
        
        return left if left else right  # 返回非空的那个结果


        