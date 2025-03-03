class Solution:
    #time:logn
    #space:O1
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        
        # 如果目标字符比数组最大字符还大，或者等于最大字符，需要返回第一个字符，因为letters本来就是升序的
        if target >= letters[-1]:
            return letters[0]
            
        while left <= right:
            mid = left + (right - left) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            elif letters[mid] > target:  # letters[mid] > target
                right = mid - 1
        
        return letters[left]
