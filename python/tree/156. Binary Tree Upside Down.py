# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    given:intput: root of a binary tree
    output:the binary tree that upside down
    idea:
    left ->root
    root->right
    right->left

    clarifying:
    -constrints of the tree node input?
    -can the input be empty/null?
    -what if only one element

    idea:
    -dfs ->subproblem 
    understand the pattern:
    first iterate to the leftmost bottom that is the new_root
    
    the new connecting logic:
    root.left.left = root.right
    root.left.right = root
    Time complexity: O(n) Each node is visited and rewired once.
	Space complexity: O(h) Due to the recursion call stack, where h is the tree height

    '''
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case:
        #call helper function
            #iteate the logic:
        if not root or not root.left:
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None#the original root subtree ,children should set to be None
        root.right = None

        return new_root
        