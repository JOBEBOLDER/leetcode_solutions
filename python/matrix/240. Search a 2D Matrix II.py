class Solution:
  # time:O(m+n)。
  #space:O1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        
        row = 0
        col = n - 1 # 从右上角开始
        while row < m and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True

            elif val > target: # 太大，往左走
                col -= 1

            else:
                row += 1 # 太小，往下走
        return False




