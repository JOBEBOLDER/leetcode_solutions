# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #initialization a result list to output result
        self.res = []#traverse need to access res, so we need to use self
        self.traverse(root)
        return self.res


    def traverse(self, root:Optional[TreeNode]):
        if root is None:
            return

        self.traverse(root.left)
        self.traverse(root.right)
        self.res.append(root.val)

'''
T:O(n)
S:O(h)

'''