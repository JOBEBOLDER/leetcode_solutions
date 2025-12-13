# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    idea:input:descriptions: List[List[int]] 
    output:TreeNode

    descriptions[i] = [parenti, childi, isLefti]
    constrct a binary tree->return the root

    clarifying:
    what 's the constrants in the input size?
    can the input->empty/null
    what edege cases ?
        float? negative? large number?


    match:
        dfs tree:
    challenge?
    - the parents not in other list parents's childen list,then that's the ultimate tree parent
        -use hashtable
    - then follow  the description to construct the tree 

    time:On
    space:On
  
    '''
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        #base case:
        if not descriptions:
            return None

        node = {}
        parent_set = set()
        children_set = set()

        def get_node(v:int)->Optional[TreeNode]:
            if v not in node:
                node[v] = TreeNode(v)
            return node[v]

        for p,c,direc in descriptions:
            parent_set.add(p)
            children_set.add(c)

            p_node = get_node(p)
            c_node = get_node(c)

            if direc == 1: #left:
                p_node.left = c_node
            elif direc == 0:
                p_node.right = c_node

        root = next(iter(parent_set - children_set))
        return node[root]

            

