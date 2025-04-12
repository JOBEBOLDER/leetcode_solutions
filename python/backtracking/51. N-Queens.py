'''
    1.need a isvalid helper function to check:the position that queen placed is isValid(row,45,135degree)
    2.mainfunction: initializae the chessboard and recall the dfs function
    3: dfs:(end condition, start dfs making choices)
    '''


class Solution:
    def solveNQueens(self, n:int) -> List[List[str]]:
        result = []
        #initialization of the chessboard
        chessboard = ['.' * n for _ in range(n)]
        self.dfs(n,0,chessboard,result)
        return [[''.join(row) for row in solution] for solution in result]



    def dfs(self,n:int,row:int,chessboard:List[str],result:List ):
        #end condition:
        if row == n:
            result.append(chessboard[:])
            return
        
        #start dfs,making choice:
        for col in range(n):
            if self.isvalid(row,col,chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                self.dfs(n,row + 1,chessboard,result)# 递归到下一行
                #backtracking:
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]


        

    #is valid or not to help us to place the queen:
    #every row, every left top(45), right top :135 degree
    def isvalid(self, row:int, col:int,chessboard:List[str]) ->bool:
        #row :
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
            

        # 检查 45 度角是否有皇后
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1

        # 检查 135 度角是否有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False  # 右上方向已经存在皇后，不合法
            i -= 1
            j += 1

        return True  # 当前位置合法

