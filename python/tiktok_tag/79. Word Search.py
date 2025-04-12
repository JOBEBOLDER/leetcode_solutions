class Solution:
    # just keep an index k to track which character of word you’re matching.
    #time:O(m * n * 4^L)
    #space:OL(length of recrusion stack )

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, 0, word):
                    return True

        return False

    def dfs(self, board:List[List[str]],i:int, j:int,k:int,word: str):
        #dfs end condtion:
        m = len(board)
        n = len(board[0])

        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
            return False
            #we found all the char in word matched
        if k == len(word) - 1:
            return True

        # Mark the cell as visited by replacing with a special char
        temp = board[i][j]
        board[i][j] = '#'  # Mark as visited
        found = (self.dfs(board, i + 1, j,k + 1,word) or 
        self.dfs(board, i - 1, j,k+1,word) or 
        self.dfs(board, i, j + 1,k + 1,word) or 
        self.dfs(board, i, j - 1,k + 1,word))

        board[i][j] = temp #backtracking ,restore the original char

        return found
