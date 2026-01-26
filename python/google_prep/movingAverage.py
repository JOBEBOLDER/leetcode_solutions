'''
Create a program that measures server latency periodically.
The program receives one latency (ping) value at a time and after each value is received, 
calculates the average latency for the latest K values.

Example values:

70, 50, 60, 50, 100 ...more values to come later
K = 5
The next value 10 comes in.
The values in window (i.e. latest `K` values) should be (50, 60, 50, 100, 10)
The next value 40 comes in. The window is now (60, 50, 100, 10, 40).

'''
from collections import deque
from typing import Optional

class MovingAverageLatency:
    def __init__(self, k: int):
        self.k = k
        self.q = deque()
        self.sum = 0

    def receive(self, val: int) -> float:
        """
        Add one latency value, return average of the latest K values.
        If fewer than K values have been received, average over what's available.
        """
        if self.k <= 0:
            return 0.0

        self.q.append(val)
        self.sum += val

        # keep only last k values
        if len(self.q) > self.k:
            old = self.q.popleft()
            self.sum -= old

        return self.sum / len(self.q)  # float average
    
#follow up:what if have to trim and remove the x largest element:
class streamAverage:
    def __init__(self,k,x):
        self.stream = deque()
        self.k = k
        self.x = x
        self.sorted_list = SortedList()

    def add_element(self,val):
        self.stream.append(val)
        self.sorted_list.add(val)
        # Maintain the size of the sliding window
        if len(self.stream) >self.k:
            removed_element = self.stream.popleft()
            self.sorted_list.remove(removed_element)

    def getAverage(self):

        if len(self.stream) < self.k:
            return 0.0
        
        trimmed_element = self.sorted_list[:-self.x]
        return sum(trimmed_element) / len(trimmed_element)



#better approach:
#time:On(qu)
#space:
'''
1) 入队 / 出队
	•	queue.append：O(1)
	•	queue.popleft：O(1)

2) SortedList 插入 / 删除
	•	self.sl.add(val)：O(log k)
	•	self.sl.remove(removed)：O(log k)

3) 求最大 x 个元素的和（瓶颈）
	•	self.sl[-actual_x:] 取切片本身就要取出 actual_x 个元素
	•	sum(...) 又要把这 actual_x 个加一遍
所以这一段是 O(actual_x)，最坏 actual_x = x，即 O(x)

✅ 总结：每次 add_element

T = O(log k + x)
最坏情况（x 接近 k）就是：
O(k)

空间复杂度（Space）

你存了：
	•	deque 最多 k 个元素 → O(k)
	•	SortedList 最多 k 个元素 → O(k)

其它变量都是常数。

✅ 总结空间

S = O(k)


'''
from collections import deque
from sortedcontainers import SortedList

class clacuateAverage:
    def __init__(self,k:int,x:int):
        self.k = k
        self.x = x
        self.queue = deque()
        self.total_sum = 0
        self.sl = SortedList()
        self.cut_sum = 0

    def add_element(self,val:int)->float:
        self.queue.append(val)
        self.sl.add(val)
        self.total_sum += val

        if len(self.queue) > self.k:
            removed = self.queue.popleft()
            self.total_sum -= removed
            self.sl.remove(removed)

        if len(self.queue) < self.k:
            return 0.0
        
        #calcualte the average
        actual_x = min(self.x,len(self.sl))
        self.cut_sum = sum(self.sl[-actual_x:]) if actual_x > 0 else 0
        self.trimmed_sum = self.total_sum - self.cut_sum
        count = len(self.sl) - actual_x #to delete number x
        return self.trimmed_sum / count if count > 0 else 0.0
    

    '''
    4. 面试官可能的 Follow-up：
    不用切片如何做到 $O(log K)$？如果面试官说 $X$ 可能很大（比如 $K=1,000,000, X=500,000$），sum(self.sl[-x:]) 就会超时。


    进阶方案：维护两个 SortedList: low (大小 $K-X$) 和 high (大小 $X$)。每次 add 一个数：先把数放进 low，更新 low_sum。如果 low 溢出了，
    把 low 最大的数挪到 high，更新两个 sum。如果 high 溢出了，把 high 最小的数删掉。这样 getAverage 
    只需要 return low_sum / len(low)，时间复杂度是 $O(1)$。
    "My initial implementation uses slicing which is $O(K)$, but if we need higher performance,
      I can use two balanced sorted sets to maintain the sum of the trimmed elements in $O(\log K)$ time."
    
    
    
    '''
#