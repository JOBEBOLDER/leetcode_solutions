class Solution:
    def reorganizeString(self, s: str) -> str:
        #medium
        #pq->max heap to find the largest element and reorganise
        #主循环：每次操作是 O(log k)，总共进行约 n 次操作，所以是 O(n log k)

        #initialization
        res = [] #to store the final result
        count = Counter(s)
       
        #但这个列表本身并不是有序的。这个列表只是为了后面的 heapq.heapify(pq) 操作做准备。
        pq = [(-freq, char) for char , freq in Counter.items(count)]

        #create heapq
        heapq.heapify(pq)
        prev = (0, "") 


        while pq:
            freq ,char = heappop(pq)
            res.append(char)

            if prev[0] < 0:
                heappush(pq, prev)

            prev = (freq + 1, char)

        if not pq and prev[0] < 0:
            return ""

        return "".join(res)

