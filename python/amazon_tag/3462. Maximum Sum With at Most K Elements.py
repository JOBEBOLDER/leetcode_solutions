class Solution:
    # medium
    '''排序每一行：O(m log m)，其中 m 是每行的最大长度
排序候选元素列表：O(nm log(nm))，其中 n 是行数，m 是每行的最大长度
总体时间复杂度：O(nm log(nm))

空间复杂度：O(n*m)，用于存储候选元素列表'''
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        res = []
        #将grid和limits一一对应
        for row ,limits in zip(grid, limits):
             #对每一行的元素进行降序排序，这样最大的元素会排在前面：
            row.sort(reverse=True)
           
            #extend() 用于 将一个列表的所有元素添加到另一个列表中。
            res.extend(row[:limits])
        res.sort(reverse = True) 
        #	reverse=True：降序排序（大到小）。默认是false，小到大
        return sum(res[:k]) #if k == 3,then :k is index:0,1,2
        