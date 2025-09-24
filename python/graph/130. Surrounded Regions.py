class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        #first step: search from the boundry , mark the boundry "O" are safe->"E"
        第二步：翻被围绕的 O
	•	现在整板扫描：
	•	看到 仍是 'O' 的 (1,1)、(1,2)、(2,2) → 这些到不了边界，翻成 X。
	•	看到 'E' 的 (3,1) → 还原成 O（它与边界相连）。
        """

        #base case:
        if not board or not board[0]:
            return 

        m = len(board)
        n = len(board[0])

        #first step: search from the boundry:safe zone:
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][n-1] == 'O':
                self.dfs(board, i, n-1)

        for  j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[m-1][j] == 'O':
                self.dfs(board, m-1, j)

        #flip the O inside
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'


    def dfs(self,board, i,j):
        m = len(board)
        n = len(board[0])

        #boundry check:
        if i < 0 or j < 0 or i >=m or j >= n :
            return 

        if board[i][j] != 'O':
            return 

        #dfs:
        board[i][j] = 'B'
        self.dfs(board, i+1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i,j+1)
        self.dfs(board,i,j-1)