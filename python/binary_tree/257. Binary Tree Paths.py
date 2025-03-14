# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #space:Oh
    #time:On
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #initialization 
        #result []->final result
        # track[] -> store the processing result
        self.result = []
        self.track = []

        if root is None:
            return self.result
        self.traverse(root)
        return self.result

    def traverse(self, root: Optional[TreeNode]):
        #递归终止条件
        self.track.append(root.val)
        if root.left is None and root.right is None:
            spath = '->'.join(map(str, self.track))
            self.result.append(spath)

        if root.left is not None:
            self.traverse(root.left)
            self.track.pop()
        if root.right is not None:
            self.traverse(root.right)
            self.track.pop()

        

    

    
