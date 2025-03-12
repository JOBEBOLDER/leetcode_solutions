# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #easy
    #binary search tree
    # preorder traverse: mid-> left-> right(recurively)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## recursively:递归
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self,root:Optional[TreeNode]):
        # interation end condition
        if root is None:
            return
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
        
        '''#迭代法iteratively：
        if root is None:
            return []
            
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            # first to process the root
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res'''


