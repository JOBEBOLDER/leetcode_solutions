import heapq
class Solution:
    '''
    [1,5],[2,6],[3,10]
        arrive  leave   chairnumber
    0   1      5          0
    1   2      6           1
    2.  3.     10

    #if the next one leave time > the next one arrive time:
    then need to assign new chair

    2 heap:
    seats_number=[] #get the smallest seats number each times
    available_seats =[] #(leave time, seats_number) #after pop the seat can re-add the seats number back into the heap
    这道题的核心矛盾是：哪些椅子是空的？哪些椅子正被人坐着？空闲椅子堆 (free_seats)：这是一个最小堆，存的是当前所有没被坐的椅子编号。
    初始状态：里面有 $0, 1, 2, 3, \dots, n$。每次有人来，从堆顶取最小的号。
    占用椅子堆 (occupied_seats)：这不仅是一个堆，还得记录“谁什么时候走”。存的是：(离去时间, 椅子编号)。每次有人来之前，先看这个堆：“有没有人的离去时间 $\le$ 当前这个人的到达时间？” 如果有，就把椅子还给 free_seats 堆。
    '''
    #time:Onlogn
    #space:On
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times.sort()

        occupied_seats = []
        seats_num = list(range(len(times)))
        heapq.heapify(seats_num)

        #begin to simulate
        for arrival,leave in times:
            while occupied_seats and occupied_seats[0][0] <= arrival:
                _,set_to_free = heapq.heappop(occupied_seats)
                heapq.heappush(seats_num, set_to_free)

            assigned_seat = heapq.heappop(seats_num)

            if arrival == target_arrival:
                return assigned_seat

            heapq.heappush(occupied_seats,(leave,assigned_seat))
        return -1

                
                    

