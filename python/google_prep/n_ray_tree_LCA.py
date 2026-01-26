def TreeNode(self,val=None,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right


def findLCA_nraytree(root:TreeNode,p:TreeNode,q:TreeNode)->TreeNode:
    #base case:
    if root is None:
        return None

    def dfs(node):
        #end condtion:
        if not root:
            return None

        if node == p or node == q:
            return node
        
        found = []  # store non-null "signals" returned from child subtrees

        for child in node.children:
            res = dfs(child)  
            # res means: in this child's subtree, we found p/q, or we already found an LCA below.
            # If res is None, this child subtree contains neither target.

            if res:
                found.append(res)
                # We got a hit from this child subtree.
                # Collecting hits lets us know how many separate subtrees contain targets.

                if len(found) == 2:
                    # If we have hits from at least two different children,
                    # it means p and q are located in different child subtrees (or one is here and one below),
                    # so the current node is the first meeting/splitting point => this node is the LCA.
                    return node

        # If we didn't get two hits:
        # - If found is empty: neither p nor q exists in this subtree => return None
        # - If found has one element: exactly one target (or an LCA found below) exists in this subtree,
        #   so we bubble that result up to the parent.
        return found[0] if found else None


