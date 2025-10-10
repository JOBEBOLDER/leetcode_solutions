class Solution:
    #这道题没啥特别的技巧，new 出来一个新的转置矩阵，其中 (x, y) 的值为原矩阵的 (y, x) 的值，直接写代码就行了。
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        res = [[0] * m for _ in range(n)]#注意这个是创建一个新的转置的matrix

        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res