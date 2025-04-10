#definition of the treenode:
class TreeNode:
    def __init__(self,val=0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right


class solution:
    def rightSideView(self, root:Optional[TreeNode])->List[int]:
        #Input: root = [1,2,3,null,5,null,4]
        #im going to use bfs:cuz we can get the node of the final node when we traverse layer by layer
        # and also the bfs will follow : add the left first and then the right subtree,so the last node that are added in the queue is the most right side node

        #base case:
        if root is None:
            return None
        
        # preparation for the bfs:
        q = deque([root])
        res = []

        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i == length - 1:
                    res.append(node.val)

                q.append(root.left)
                q.append(root.right)

        return res



        