class Solution:
    '''
    time:Logn
    space:O1
    #main idea:在升序排列的字符数组 letters 中，找出严格大于 target 的最小字母。如果找不到（也就是 target ≥ 所有字母），就返回第一个字母（wrap around）。
    '''
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if not letters:
            return None
        left = 0
        right = len(letters) - 1

        if target >= letters[-1]:
            return letters[0]

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1

            elif letters[mid] > target:
                right = mid - 1

        return letters[left]
