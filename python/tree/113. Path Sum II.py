# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    given: input: root,int :targetsum
    output: list[[int,int]-> the node on these tree sum ==target

    clarifying:
    - empty input/None
    - one element
    - what are the contraints of the input size?
    - what other edgr cases tha i should be arare of ,target sum-> negative? 0? float?
    idea:
这题之所以看起来是 preorder，不是因为“遍历顺序必须叫 preorder”，而是因为你在做的是 沿着根到叶子的路径做状态更新——这个状态（track 和 remain）必须在“进入节点时”就更新，才能正确传给孩子。

    '''
    def __init__(self):
        self.res = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.dfs(root,targetSum,[])
        return self.res


    def dfs(self,root,remain,track):
        if not root:
            return 
        
        #这个状态（track 和 remain）必须在“进入节点时”就更新，才能正确传给孩子。
        track.append(root.val)
        remain -= root.val

        if not root.left and not root.right and remain == 0:
            self.res.append(track[:])

        self.dfs(root.left,remain,track)
        self.dfs(root.right,remain,track)

        track.pop()
