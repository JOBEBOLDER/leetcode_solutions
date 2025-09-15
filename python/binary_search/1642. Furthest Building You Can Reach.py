class Solution:
    #	•	最小堆：堆里存“梯子使用的最大差值们”，小的差值弹出去用砖头。
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minheap = []
        n = len(heights)

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            if diff > 0: #we need to use the ladders:
                heapq.heappush(minheap, diff)

            if len(minheap) > ladders:
                min_diff = heapq.heappop(minheap)
                bricks -= min_diff
                ## 砖也不够，不能去 i+1
                if bricks < 0:
                    return i

            

        return n-1  # 能一路走到最后
