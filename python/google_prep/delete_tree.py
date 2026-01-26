
'''You are given a binary tree, and a list of nodes to delete.
After deleting all nodes in to delete, we are left with a forest - disjoint union of one or more trees).

Return a list with a representation of each of these trees.

Note: The representation of the tree is a list that follows a slightly 
modified heap pattern: [root, root-left, root-right, root-left-left, root-left-right, root-right-left, ...].

For any index i you can find its left child at 2i + 1 and right at 2i + 2.

   1
 2  3
4     5
1
time:On 
space:On + k
output:[]

Example 1: 
Input: tree = [1,2,3] to_delete= [1]
Output = [[2],[3]]


Ex 2:
Input: tree = [1,2,3] to_delete= [2]
Output = [[1, null, 3]]

Ex 3:
Input: tree = [1,2,3] to_delete= [2,3]
Output = [[1]]
'''
class 
