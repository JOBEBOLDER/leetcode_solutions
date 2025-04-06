class Solution:
    '''
   1. ----   -----
   2. ------
        ---
    3.------  
    '''
    #time:On
    
    #space:On
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key = lambda x:x[0])

        #choose the first element of each array as increasing order
        res.append(intervals[0])

        for i in range(1,len(intervals)):
            curr = intervals[i]
            last = res[-1]
            if curr[0] <= last[1]:
                last[1] = max(curr[1],last[1])
            else:
                res.append(intervals[i])

        return res