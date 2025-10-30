class Solution:
    '''
    understand:
    if the later lake it's raining again ,then it will flood
    example:
    [1,2,3,4] = -1,-1,-1,-1
    [-1,-1,2,1,-1,-1]
    [1,2,0,1,2]


    '''
    def avoidFlood(self, rains: List[int]) -> List[int]:
        #my idea:
        #the main idea is to create a full array that can mark the index of the rain day
        #and dry days array to mark the index, so can can know that two 重复的湖，比如2，0，2，两个湖之间有dryday可以抽水

        ans = []
        full = {}  # mark the lake raining day index
        dry_days = []  # ordered array

        for i in range(len(rains)):
            # if it's a rainy day
            if rains[i] > 0:
                lake = rains[i]  # 建议用变量存储，更清晰
                
                # if the lake already rained before
                if lake in full:
                    # check if we have dry day between two rains
                    pos = bisect.bisect_right(dry_days, full[lake])
                    #   ^^^ 用 pos，不是 day
                    
                    if pos == len(dry_days):
                        return []  # cannot find suitable dry day
                    
                    # use this dry day to dry the lake
                    day = dry_days[pos]
                    ans[day] = lake
                    dry_days.pop(pos)
                
                # update the lake's last rain day
                full[lake] = i
                ans.append(-1)  # ← 移到外面！不管是否重复都要 append
                
            # if it's a dry day
            else:
                dry_days.append(i)
                ans.append(1)  # ← 添加占位符！

        return ans
