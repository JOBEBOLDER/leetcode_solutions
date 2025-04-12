# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #time:On+On
    #space:Oh
    def __init__(self):
        self.parent = {}
    #we need a traverse function to find the target first, then do bfs from the target point
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #traverse all the node and record their parent
        self.traverse(root, None)

        #start form the target node do bfs
        q = deque()
        q.append(target)
        #we also need a set to record the visited node:
        visited = set() 
        visited.add(target.val)

        dist = 0 #record the current distant
        res = [] #the output

        while q:
            length = len(q)
            for i in range(length):
                cur = q.popleft()
                if dist == k:
                    res.append(cur.val)
                
                #do the bfs,left node and right node:
                '''37-40这行，为什么和传统bfs不一样，多了这几行
                因为传统 BFS 只从上往下（比如从根往子节点）走，
                而这题要找的是离某个目标点为 k 距离的所有点，
                所以我们需要从目标点 target 出发，向上也能走 —— 要能走“父节点”！'''
                parentNode = self.parent.get(cur.val)
                if parentNode and parentNode.val not in visited:
                    visited.add(parentNode.val)
                    q.append(parentNode)

                if cur.left and cur.left.val not in visited:
                    visited.add(cur.left.val)
                    q.append(cur.left)
                if cur.right and cur.right.val not in visited:
                    visited.add(cur.right.val)
                    q.append(cur.right)
            dist += 1
            if dist > k:
                break
        return res

    def traverse(self, root, parentNode):
        if root is None:
            return None

        self.parent[root.val] = parentNode
        self.traverse(root.left, root)
        self.traverse(root.right, root)

'''
visited 里放的是值（int），因为我们只关心是否访问过；
queue 里放的是 TreeNode 节点对象，因为我们还要继续访问它的左右子树。
'''
