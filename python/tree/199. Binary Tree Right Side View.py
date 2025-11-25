# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    思路记错了，要用bfs，queue做
    time:On
    space:Oh
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #base case:
        if root is None:
            return []

        queue=deque()
        queue.append(root)
        res = []

        while queue:
            sz = len(queue)
            for i in range(sz):
                # ⬅️ 从队列取一个 node 出来（否则你根本不知道你在处理谁）
                node = queue.popleft()
                if i == sz - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


    