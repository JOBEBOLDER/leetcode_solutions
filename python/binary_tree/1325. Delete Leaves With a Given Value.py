# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    understand:
    only delete the leaf node == target.val

    leaf node:postorder

    time
    '''
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #edge case:
        if not root or not target:
            return None

        def dfs(node):
            #base case:
            if node is None:
                return

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            #postorder delete the node:
            if not node.left and not node.right and node.val == target:
                return None

            return node

        return dfs(root)


        