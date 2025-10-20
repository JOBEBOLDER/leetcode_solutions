class Solution:
    #构造相反数，当到了中间+0
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)
        if n % 2 == 1:
            ans.append(0)
        return ans


#时间复杂度：O(N)。

#空间复杂度：O(1)，除了存储答案的数组 ans 之外，额外的空间复杂度是 O(1)。