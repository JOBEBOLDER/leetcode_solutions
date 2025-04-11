class Solution:
    #time:Om*n
    #space:Om*n
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        upper_bound = 0
        lower_bound = m - 1
        left_bound = 0
        right_bound = n - 1

        res = [] #store the final result

        while len(res) < m * n: #ifit's equal,then we need to add one more element
            #left->right
            if upper_bound <= lower_bound:
                for i in range(left_bound, right_bound + 1):
                    res.append(matrix[upper_bound][i])
                upper_bound += 1
            
            #up -> low
            if left_bound <= right_bound:
                for j in range(upper_bound,lower_bound + 1):
                    res.append(matrix[j][right_bound]) #j changing, right_bound keep the same
                right_bound -= 1

            #right -> left:
            if upper_bound <= lower_bound:
                for i in range(right_bound, left_bound - 1, -1):
                    res.append(matrix[lower_bound][i])
                lower_bound -=1

            #low->up
            if left_bound <= right_bound:
                for j in range(lower_bound,upper_bound -1, -1):
                    res.append(matrix[j][left_bound])#j changing, left_bound keep the same
                left_bound += 1

        return res
