class Solution:
    '''🔢 一、时间复杂度：O(n!)

这是因为：
	•	每一行你都要尝试在某一列放置一个皇后。
	•	每一行最多尝试 n 列，但随着皇后越来越多，可选的位置会越来越少（因为列、对角线被限制了）。
	•	所以总共是一个 排列问题，最多是 n! 种可能（第1行n种选择，第2行最多n-1，依此类推）。

✅ 这就是经典 N 皇后问题的复杂度：O(n!)


space:On*n

'''
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        chessboard = ['.' * n for _ in range(n)]
        self.dfs(n,0,chessboard,result)
        return [[''.join(row) for row in solution ]for solution in result]

    def dfs(self, n:int ,row:int ,chessboard:List[str],result:List):
        #dfs end condition:
        if row == n:
            result.append(chessboard[:])
            return 
        for col in range(n):
            if self.isvalid(row, col,chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col + 1:]
                self.dfs(n,row + 1,chessboard,result) #move tho the next line
                #backtracking:
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col + 1:]


    
    def isvalid(self, row:int ,col:int,chessboard:List[str])->bool:
        #row:
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False

        i,j = row - 1,col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i,j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True