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
