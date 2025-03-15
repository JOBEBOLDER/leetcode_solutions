# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #time:On
    #空间复杂度：O(w)，其中w是树的最大宽度，最坏情况下为O(n)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if root is None:
            return res

        # 使用队列进行BFS层序遍历
        q = deque([root])
        
        # 逐层遍历二叉树
        while q:
            size = len(q)  # 当前层的节点数量
            
            # 遍历当前层的所有节点
            for i in range(size):
                node = q.popleft()
                
                # 当前层的最后一个节点（即最右侧节点）加入结果
                if i == size - 1:
                    res.append(node.val)
                
                # 先将左子节点入队，再将右子节点入队
                # 这样确保同一层的节点从左到右排列
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res