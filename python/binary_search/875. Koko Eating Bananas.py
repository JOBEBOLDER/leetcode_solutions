class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 1000000+1

        while left < right:
            mid = left + (right - left) // 2
            if self.check(piles,mid) <= h:
                #如果可以在h小时内吃完，就继续找minimum
                right = mid 
            else:
                left = mid + 1
        return left


    def check(self,piles,speed):
        time = 0
        for pile in piles:
            time += pile // speed
            if pile % speed > 0:
                time += 1

        return time
