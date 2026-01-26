'''
Reverse Odd Levels of Binary Tree

Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.
For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.
A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.
The level of a node is the number of edges along the path between it and the root node.


input:
root: binary tree
goal:everse the node values at each odd level of the tree.

return :root (node)

UMPIRE:

clarifying:
tree:perfect binary tree

        2
     1       3 
4    7.   11.   29
dfs(node,level)
if level == odd:
    dfs()

levvel = 0
[3,1]
queue:[1,3]
res.append(reversed[queue])

dfs:
return dfs()





time:On
space:Oh

EDGE CASEs：
- emptyroot: rasie errors: None
- dfs,bfs
-hit: odd level:
queuu:pop 
res:append.node(reversed) 

        2
     3      1
4    7.   11.   29

queue[3,1]
   cur_level = 2

   
feedback:
-讲题框架
-看题要看清楚
-复习下bfs，
-dfs 
list[string]-,emtpty,e
int:float,
tree:BST,

'''
from collections import deque
class TreeNode:
    def __init__(self,left=None,right=None,val = None):
        self.val= val
        self.left = left
        self.right = right

class Solution:
    def reverse_odd_level(self,root:TreeNode)->TreeNode:
        #edge cases:
        if not root:
            return None
        
        #bfs:
        queue = deque()
        cur_level = 0
        queue.append(root)

        while queue:
            if cur_level % 2 != 0:
                reversed = queue[::-1]
                #append the revered order of the treenode to the original parentnode
                
                cur_level +=1
            else:
                length = len(queue)
                for _ in range(length):
                    cur = queue.popleft()
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                cur_level += 1
        return root
        


                



                



