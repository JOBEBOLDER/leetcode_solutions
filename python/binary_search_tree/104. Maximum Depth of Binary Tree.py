# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #ease
    #binary search tree: maximum :use res to store the variable
    #dfs 做法：
    def __init__(self):
        self.res = 0
        self.depth = 0
    def maxDepth(self,  root: Optional[TreeNode]) -> int:
        self.dfs_traverse(root)
        return self.res

    def dfs_traverse(self, root:Optional[TreeNode]):
        if root is None:
            return 

        self.depth += 1

        self.res = max(self.depth, self.res)
        self.dfs_traverse(root.left)
        self.dfs_traverse(root.right)

        self.depth -= 1

#bfs做法：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 0
        queue = collections.deque([root])
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth