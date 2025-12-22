# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    understadnging:
    root of the tree
    return max_average of the subtree

    edge case:
        -root is empty/null

    match:
        dfs tree?

    plan:
        postorder:
        dfs()
        -cur_sum of the subtree
        -cur_num of the subtree node   
    
    time:On:every node of the tree
    space:Oh:recursion stack

    '''
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if root is None:
            return 0
        max_average = float("-inf")
        

        def dfs(node):
            nonlocal max_average
            #base case:
            if node is None:
                return 0,0

            cur_leftsum,cur_leftnum = dfs(node.left)
            cur_rightsum,cur_rightnum = dfs(node.right)

            total_sum = cur_leftsum + cur_rightsum + node.val
            total_num = cur_leftnum + cur_rightnum + 1
            max_average = max(max_average,total_sum / total_num)

            return total_sum,total_num

        dfs(root)
        return max_average


        