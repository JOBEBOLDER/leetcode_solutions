# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    understanding:
    root: binary tree
    target: find the biggest BST subtree(have the max number of nodes)
     quesitons:
     edge cases:
        -root: empty/null->0/None/error
    match:
        -dfs postorder 
    plan:
    Key idea

        At each node, I want to know whether the subtree rooted at this node is a BST.

        To verify that efficiently, I need more than just “left and right are BST” — I also need:
            •	the maximum value in the left subtree
            •	the minimum value in the right subtree

        So I’ll do a postorder DFS (bottom-up), and for each node I return a package of info.
    time:On
    space:Oh
    '''
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')
        if root is None:
            return 0
        def dfs(node): #return 4 items:(is_bst,size,min_val,max_val)
            #base case:
            nonlocal ans
            if not node:
                return True,0,float('inf'),float("-inf")
            l_bst,l_size,l_min,l_max = dfs(node.left)
            r_bst,r_size,r_min,r_max = dfs(node.right)

            # BST 条件：左右都是 BST + 左最大 < 当前 < 右最小
            if l_bst and r_bst and l_max < node.val < r_min:
                size = l_size + r_size + 1
                ans = max(ans,size)
                mn = min(l_min,node.val)
                mx = max(r_max,node.val)
                return True,size,mn,mx
            
            return False,0,0,0

        dfs(root)
        return ans

            
            

