class Solution:
    #medium + 
    #sliding window
    #time:On,space:?
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = [0, 0]
        #g只能是0/1
        max_s1 = 0


        for i,(c,g) in enumerate(zip(customers,grumpy)):
            s[g] +=  c   #根据0/1统计满意和不满意的顾客数量

            if i < minutes - 1:  # 窗口长度不足 minutes
                continue

            #先更新最大值
            max_s1 = max(max_s1,s[1])

            #再对左边元素进行处理，索引是从1mins开始！！！
            if grumpy[i - minutes + 1] == 1:
                s[1] -= customers[i - minutes + 1]  # 窗口最左边元素离开窗口
        return s[0] + max_s1



            
