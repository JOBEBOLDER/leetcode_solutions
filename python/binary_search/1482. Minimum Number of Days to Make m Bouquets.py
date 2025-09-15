'''
	1.	设定搜索区间 [min(bloomDay), max(bloomDay)]，范围大小记作 R。
	2.	在这个区间里二分查找最小可行天数。
	3.	每次二分时，用一次 canMake 来判断某一天是否可行。
# Time:
# O(n * log(max(bloomDay)))
# Space:
# O(1) (in-place, no extra memory)
'''


class solution:
    def mindays(self,bloomDay:List[int],m:int,k:int) ->int:
        #base case:
        if len(bloomDay) < m*k:
            return -1
        
        left = 1
        right = max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2
            if self.canmake(bloomDay,mid,m,k):
                right = mid
            else:
                left = mid + 1

        return left



    def canmake(self,bloomDay,days,m,k):
        flowers = 0
        bouquets = 0

        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0

            else:
                flowers = 0

            if bouquets == m:
                break

        return bouquets >= m
