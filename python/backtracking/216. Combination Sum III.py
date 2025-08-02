class Solution:
    #time:O(2^9)
    #space:Ok(how many stack you used)
    #this question is almost the same as the leetcode77, the only difference is we need one more condition,the sub combination 
    #we need to varfify it's == k

    def __init__(self):
        self.level = []
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #we recall the backtracking function here
        self.backtracking(k,n,1)
        return self.res


    def backtracking(self,k,n,start):#you need the start to know when we should start for the next round recursion(backtracking)
    # base case, when we should stop the backtracking and collect the result
        if len(self.level) == k:
            #only collect it when it sum == n:
            if sum(self.level) == n:
                self.res.append(self.level.copy())
            return 

        #repeating pattern, do backtracking 
        for i in range(start,10):
            self.level.append(i)
            #optimize# 剪枝：如果当前路径和已经超过 n，没必要继续
            if sum(self.level) <= n:
                self.backtracking(k,n,i+1)

            self.level.pop()
