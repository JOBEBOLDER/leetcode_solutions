# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # bfs-> traverse the tree layer by layer
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        if root is None:
            return 0

        #initialization
        q = deque([root])
        depth = 1

        # traverse
        while q:
            sz = len(q)

            for i in range(sz):
                cur = q.popleft()
                ## minDepth - 找到第一个叶子节点就返回
                if cur.left is None and cur.right is None:
                    return depth

                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            depth += 1
        return depth



        

        