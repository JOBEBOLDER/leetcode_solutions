class Solution:
    #time:On
    #space:O1
    def __init__(self):
        self.res = []
    def lexicalOrder(self, n: int) -> List[int]:
        # 总共有 9 棵多叉树，从 1 开始
        for i in range(1, 10):
            self.dfs(i, n)
        return self.res

    def dfs(self, root:int, n:int):
        #base case:
        if root > n:
            return

        self.res.append(root)

        for child in range(root * 10, root * 10 +10):
            if child > n:
                break
            self.dfs(child, n)
        
        
