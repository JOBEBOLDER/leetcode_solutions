# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    难点是如何考虑四周感染：
    用parent = {} dict 建立映射：child
    假设有边 1 -> 2（2 是 1 的左孩子），字典里就有：
	•	parent[2] = 1

    所以从任意节点扩散时，需要check 三个方向的点
        •	node.left
        •	node.right
        •	parent.get(node)  （父节点）

    the given start:is a int
    '''
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        #edge case:
        if not root:
            return 0
        time = -1
        queue=deque([root])
        parent = {}

        #first time bfs,build the releationship 
        start_node = None
        while queue:
            cur = queue.popleft()
            if cur.val == start:
                start_node = cur

            if cur.left:
                parent[cur.left] = cur
                queue.append(cur.left)

            if cur.right:
                parent[cur.right] = cur
                queue.append(cur.right)

        #second bfs: calculate the time:
        q = deque([start_node])
        seen = {start_node}
        while q:
            length = len(q)
            for _ in range(length):
                cur = q.popleft()
                for nei in (cur.left,cur.right,parent.get(cur)):
                    if nei and nei not in seen:
                        seen.add(nei)
                        q.append(nei)
            time += 1

        return time

            

        

        