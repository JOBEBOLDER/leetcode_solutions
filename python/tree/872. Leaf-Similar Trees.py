# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #my approach:
    # using dfs, traverse 2 tree separately and then output the leave node accordingly in tree1[] and tree2[]
    #and then compare these two array are the same or not
    #probably we need a helper function to dfs the tree
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = self.dfs(root1,[])
        tree2 = self.dfs(root2,[])

        return tree1 == tree2


    def dfs(self, node:TreeNode,node_list:list):
        #dfs end condtion:
        if not node:
            return node_list
        if not node.left and not node.right:
            node_list.append(node.val)
            return node_list
        # 递归遍历左右子树（先左后右，保证从左到右的顺序）
        self.dfs(node.left, node_list)
        self.dfs(node.right,node_list)
        return node_list

