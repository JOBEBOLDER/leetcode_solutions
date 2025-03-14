# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #时间复杂度: O(n)

    '''在最坏情况下，我们可能需要遍历整棵树（如果树是非常不平衡的）
    在平均情况下，BST的搜索时间复杂度是 O(log n)，但题目只要求分析最坏情况

    空间复杂度: O(h)在最好情况下（完全平衡二叉树），h = log n，空间复杂度为 O(log n)'''
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #what is the number of the root,what if is a empty tree?
        #what is the range of the value? what if a negative number or ==0?

        if not root or root.val == val: 
            return root

        if val > root.val:
            return self.searchBST(root.right, val)

        if val < root.val:
            return self.searchBST(root.left, val)

        return root


    