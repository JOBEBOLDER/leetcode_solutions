# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #medium
    #dfs: res track the processing value
    #time:On
    #space:Oh
    def __init__(self):
        self.sum = 0

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, None, None)
        return self.sum

    def dfs(self, root: Optional[TreeNode],parents:Optional[TreeNode],grandparents:Optional[TreeNode]):
        #dfs base case:
        if root is None:
            return 

        # If grandparent has even value, add current node's value to sum
        if grandparents and grandparents.val % 2 == 0:
            self.sum += root.val
            
        # dfs recursive calls - pass updated relationships
        self.dfs(root.left, root, parents)   # root becomes parent, parent becomes grandparent
        self.dfs(root.right, root, parents)  # for the child nodes
        