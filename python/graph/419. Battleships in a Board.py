class Solution:
    # A cell is the "head" of a battleship if:
    # - it is 'X'
    # - there is no 'X' directly above or to the left
    # Because we scan from top-left to bottom-right,
    # the first cell of each ship will be its unique top-left cell.

    #time:O*n
    #space:O1
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                #if we can not find it
                if board[i][j] != 'X':
                    continue
                #if we foudn the battleships, check the condition,if they are not satisfies ,then continue
                #check the top and the left
                if i > 0 and board[i-1][j] == 'X':
                    continue

                if j > 0 and board[i][j - 1] == 'X':
                    continue

                #if all the conditions that mention above not satifised ,then we can build battleships
                res += 1

        return res
                

        
