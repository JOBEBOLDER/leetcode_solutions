class Solution:
    #medium
    #时间复杂度：O(N−K)，这里 N 是数组的长度；空间复杂度：O(1)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #cuz we are gonna keep k number element
        n = len(arr)
        #we are gonna exclude delete_num's element
        delete_num = n - k

        left = 0

        right = n - 1

        while delete_num:
            #it means when the value is equal, choose the front one
            if abs(x - arr[left]) <= abs(x-arr[right]):
                right -= 1

            else:
                left += 1
            delete_num -= 1
        return arr[left : left + k]
