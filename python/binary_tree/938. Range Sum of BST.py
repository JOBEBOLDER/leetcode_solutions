# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #time:On
    #space:OH
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #base case 
        if root is None:
            return 0

        #initiallize the sum:
        curSum = 0

        if low <= root.val <= high:
            curSum += root.val

        curSum += self.rangeSumBST(root.left, low, high)
        curSum += self.rangeSumBST(root.right, low, high)

        return curSum



