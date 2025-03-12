# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #medium
    # binary tree level order traversal->本质是BFS
    #通过队列模拟
    #迭代的 BFS 需要使用队列（Queue）：
    #空间复杂度是 O(w)，其中 w 是树中最宽的层的节点数。对于一般形状的树，w 通常可以近似为 O(h)。时间复杂度是 O(n)：因为每个节点只被处理一次。
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        dq = deque()
        dq.append(root)
        res=[]
       

        while dq:
            sz = len(dq)
            level = []
            for i in range(sz):
                node = dq.popleft()
                level.append(node.val)
                if node.left is not None:
                    dq.append(node.left)
                if node.right is not None:
                    dq.append(node.right)
            res.append(level)
        return res



