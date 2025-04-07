class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #use minheap,
        # if the last one endtime is smaller than the next one starting time ,that means that we can reuse the meeting room ,then we can just pop the last one ,keep the len unchange
                #resuable
                #上一个结束时间小于后一个开始时间，说明可以复用，直接删除现在的meeting，代表meetingroom个数不变
                # room[0]->minheap the NO.1 element
                #“min heap堆存结束时间，来了新会议，能复用就 pop，不能复用就加房间。”

        #time:Sorting intervals takes O(n log n)
        #space:	In the worst case, all meetings overlap → heap size becomes n,So heap can grow to O(n)
        #base case:
        if not intervals:
            return 0

        intervals.sort(key = lambda x:x[0])

        room = [] #minheap

        for i in range(len(intervals)):
            processing = intervals[i]
            if not room:
                heapq.heappush(room,processing[1]) #store the first element ending time

            #check the condition :if the minheap min element(the earlist time) less then the following one starting time,then we can pop,means that we can reuse the room 
            else:
                if room[0] <= processing[0]:
                    heapq.heappop(room)

                heapq.heappush(room, processing[1])

        return len(room)
