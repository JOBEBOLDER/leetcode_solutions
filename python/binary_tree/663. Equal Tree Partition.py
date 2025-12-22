# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    do a dfs first calculate the whole tree value->total sum of the tree

    dfs the tree again:
    we are gonna find a subtree == total sum // 2
    once we find this subtree value, then we do (totoal sum-subtree value) != another subtree  value->return false,otherwise: true
But I must ensure node is not root, because cutting at the root doesn’t remove any edge and wouldn’t produce two non-empty trees.
	•	Time：不是 O(2n)（虽然你做了两次 DFS），大 O 里常数要忽略，所以是 O(n)。
	•	Space：也不是 O(1)，因为递归 DFS 有调用栈，最少 O(h)（h 是树高；最坏链状树就是 O(n)）。
    
    '''
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        self.total_sum = 0
        self.dfs(root)

        #total_sum can not split into 2 integer
        if self.total_sum % 2 != 0:
            return False
        
        target_sum = self.total_sum // 2
        self.found = False
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            s = left+right+node.val
            
            if s == target_sum and node is not root:
                self.found = True
            return s
        dfs(root)
        return self.found


    def dfs(self,root):
        #base case:
        if root is None:
            return 0

        self.total_sum +=root.val
        self.dfs(root.left)
        self.dfs(root.right)

        