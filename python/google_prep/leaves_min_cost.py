'''
1365. Minimum Cost to Disconnect Leaves
Medium
You are given a binary tree where each edge has a non-negative integer weight. The tree is rooted at node 1. A leaf is defined as a node that does not have any children. Your task is to determine the minimum total cost (i.e., sum of the weights of the selected edges) required to "cut" the tree such that all leaf nodes become disconnected from the root.

Cutting an edge means removing that edge from the tree. When an edge is cut, all nodes in the subtree rooted at the child of that edge become disconnected from the root. Your goal is to choose a set of edges to cut such that after the removals, there is no path from the root to any leaf, and the total cost is minimized.

Input Format:

The first line contains an integer N representing the number of nodes in the tree.
The following N-1 lines each contain three integers u, v, w, meaning there is an edge between node u and node v with weight w.
(It is guaranteed that the given edges form a valid tree with node 1 as the root.)
Output Format:

Print a single integer representing the minimum cost required to disconnect all leaves from the root.
Constraints:

1 ≤ N ≤ 10^5
0 ≤ w ≤ 10^4
Example:

Input:

4
1 2 5
1 3 1
2 4 10

Output:
6

Explanation:

The binary tree structure is as follows:
     1
    / \
   2   3
  /
 4

Total cost = 5 + 1 = 6.

'''

def min_cut_to_disconnect(edges):
    adj = defaultdict(list)
    for 