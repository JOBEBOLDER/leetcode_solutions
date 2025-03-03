class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ans = j = 0
        for x in arr1:
            while j < len(arr2) and arr2[j] < x - d:
                j += 1
            if j == len(arr2) or arr2[j] > x + d:
                ans += 1
        return ans