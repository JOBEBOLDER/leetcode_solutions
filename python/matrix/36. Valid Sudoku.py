from typing import List
#time:On*m
#space:On*m
#	但对 LeetCode 36 这种 固定 9×9：
# n,m 都是常数，所以严格说 Time = O(1)，Space = O(1)。
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxex = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]

                if num == '.':
                    continue

                box_id = (i // 3)*3 + (j//3)

                if num in rows[i] or num in cols[j] or num in boxex[box_id]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxex[box_id].add(num)
        return True