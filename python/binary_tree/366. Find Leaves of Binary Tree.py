# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    
        Approach: postorder DFS

    I run a postorder DFS that returns the bottom-up height:
        •	If node is None, return -1
    (so that a leaf becomes max(-1, -1) + 1 = 0)
        •	Compute:
        •	lh = dfs(node.left)
        •	rh = dfs(node.right)
        •	h = max(lh, rh) + 1

    Then I append node.val into res[h].
    If res doesn’t have a bucket for height h yet, I create it.

    Finally, I return h upward.
    '''
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node):
            if not node:
                return -1

            l_height = dfs(node.left)
            r_height = dfs(node.right)
            h = max(l_height,r_height) + 1

            while len(res) <= h:
                res.append([])
            res[h].append(node.val)

            return h

        dfs(root)
        return res