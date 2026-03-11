'''
Coding: Find the cheapest common ancestor for two nodes in a tree. 
Each node of the tree has a price and knows its parent and children. 
You are provided with two different nodes of the tree and you must find the one with 
the cheapest price among all the common ancestors. (Talked about brute force, coded out,
 asked for TreeNode class setup, asked for TC, dry run with an example,
   asked for test cases / edge cases, 
asked for optimal solution (out of time so only asked about ideas and TC))
'''

class TreeNode:
    def __init__(self,val,parent,children,price):
        self.val = val
        self.parent = parent
        self.children = []
        self.price = price


    def find_cheapest_common_ancestor(self,node_a:TreeNode, ndoe_b:TreeNode)-> TreeNode:
        if not node_a or not node_b:
            return None
        
        ancestors_a = set()
        cur = node_a
        while cur:
            ancestors_a.add(cur)
            cur = cur.parent

        cheapest_node = None
        cheapest_price = float('inf')

        cur = node_b
        while cur:
            if cur in ancestors_a:
                #find a LCA:
                if cur.price < cheapest_price:
                    cheapest_price = cur.price
                    cheapest_node = cur
                cur = cur.parent
        return cheapest_node if cheapest_node not None else -1