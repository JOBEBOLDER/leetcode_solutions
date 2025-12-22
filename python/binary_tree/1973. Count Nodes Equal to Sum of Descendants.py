# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    root: 
    descendant sum == parent node

    return the num of node that meet these requirement
    
    postorder 
    '''
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
        #base case:
        if not root:
            return 0

        ans = 0
        cur_sum = 0

        #postorder:
        def dfs(node):
            nonlocal ans
            if node is None:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            cur_sum = left_sum + right_sum
            if cur_sum == node.val:
                ans += 1
            #返回子树的结果sum
            return node.val+left_sum+right_sum
        
        dfs(root)

        return ans

        


