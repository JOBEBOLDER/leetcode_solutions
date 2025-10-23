class Solution:
    '''
    umpire:
    understand:
    input: nested list, and a interger
    trips[0] = [2,1,5],2 passengers, from 1-5
    output: boolean,true can pick and drop all the passengers

    first example:
    trip1:2 people, from 1 to 5
    trip2: 3 people, from 3 to 7

    but because no one get off from the last trip, 2+3>cap(4) -> false

    second example:
    trip1:2 people, from 1 to 5
    trip2: 3 people, form 3 to 7 

    2+3 >=5 ->true

     这是一个「区间事件变化」问题。
✔️ 关键思想是 前缀和 / 差分数组 / 扫描线。
✔️ 以后看到“从某点到某点”的变化统计（例如：

“I need to keep track of how the passenger count changes over time,
so a difference array (or sweep line) fits perfectly.”
当 from == previous.to 时：
	•	默认约定是「前一批人先下车，后一批人再上车」。
	•	所以 timeline[end] -= num 和 timeline[start] += num 这种写法天生就支持这种“瞬时交接”。
    
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timeline = [0] * 1001  #因为索引从0开始，所以你需要+1，才有1000个arrays

        for nums, start, end in trips:
            timeline[start] += nums
            timeline[end] -= nums

        cur = 0
        for x in timeline:
            cur+= x # # 这一步是前缀和：在这个时间点上的实际人数
            if cur> capacity:
                return False
        return True