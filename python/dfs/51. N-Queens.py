class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        chessboard = ['.' * n for _ in range(n)]
        self.dfs(n,0, chessboard, res)
        return res



    def dfs(self,n,row,chessboard,res):
        #backtracking end condition:
        if row == n:
            res.append(chessboard[:])
            return 

        #dfs repeat Pattern
        for col in range(n):
            if self.valid(row,col,chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                self.dfs(n,row+1,chessboard,res)
                #backtracking:
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]


    def valid(self,row,col,chessboard):
        #check for 3 directions:row, left top, right top:
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False


        #check for left top:
        i = row - 1
        j = col - 1
        while i >= 0  and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i-=1
            j-=1

        #check right top:
        i = row -1
        j = col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False
            i-=1
            j +=1

        return True
