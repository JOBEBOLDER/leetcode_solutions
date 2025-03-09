class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 获取图像的行数和列数
        rows, cols = len(image), len(image[0])
        # 记录起始像素的原始颜色
        originalColor = image[sr][sc]
        
        # 如果新颜色和原始颜色相同，直接返回，不需要修改
        if originalColor == color:
            return image
        
        # 定义DFS函数
        def dfs(r, c):
            # 检查坐标是否在图像范围内，以及当前像素颜色是否为原始颜色
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != originalColor:
                return
            
            # 将当前像素颜色修改为新颜色
            image[r][c] = color
            
            # 递归处理上下左右四个方向的相邻像素
            dfs(r+1, c)  # 下
            dfs(r-1, c)  # 上
            dfs(r, c+1)  # 右
            dfs(r, c-1)  # 左
        
        # 从起始位置开始DFS
        dfs(sr, sc)
        return image