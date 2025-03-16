# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #medium
    # solutions: if only appear once odd number,it's mean we can construct a valid palind,
    #time:On
    #space:O1
    def __init__(self):
        self.count = [0] * 10
        self.res = 0
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root:Optional[TreeNode]):
        #dfs base case
        if root is None:
            return 

        self.count[root.val] += 1
        #dfs end condition
        # dfs end condition - leaf node
        if root.left is None and root.right is None:
            
            odd = 0
            for n in self.count:
                if n % 2 == 1:  # Fixed condition to properly check odd counts
                    odd += 1
            
            if odd <= 1:
                self.res += 1

        #dfs traverse 
        else:
            self.dfs(root.left)
            self.dfs(root.right)

        self.count[root.val] -= 1



