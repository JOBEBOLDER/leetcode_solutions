'''
Google Interview Screening Question: Windowed Average Excluding Largest K
Screening
Problem
Given an integer array nums, a window size windowSize, and an integer k, 
return a list of averages for each sliding window of size windowSize as the window moves 
from left to right. When calculating each window’s average, ignore the largest k numbers inside that window.

Example
Input:

nums = [10, 20, 30, 40, 50, 60]  
windowSize = 3  
k = 1
Output:

[15.0, 25.0, 35.0, 45.0]
Explanation:

Window [10, 20, 30]: remove largest (30) → (10 + 20) / 2 = 15.0

Window [20, 30, 40]: remove largest (40) → (20 + 30) / 2 = 25.0

Window [30, 40, 50]: remove largest (50) → (30 + 40) / 2 = 35.0

Window [40, 50, 60]: remove largest (60) → (40 + 50) / 2 = 45.0

Suggested Approach
Use a sliding window of size windowSize with two heaps (min-heap and max-heap) or
 an ordered multiset to efficiently track the k largest elements.

Maintain the sum of all elements in the window. 
Subtract the contribution of the k largest when computing the average.

Slide the window forward by removing the outgoing element and 
inserting the new element while updating both heaps and the sum.

Time & Space Complexity
Time: O(n log windowSize), due to heap operations per element.

Space: O(windowSize), for maintaining heaps and window data.


'''

from collections import deque
from sortedcontainers import SortedList # 面试时如果没库，建议口述平衡树逻辑

def windowed_average_exclude_k(nums, windowSize, k):
    if not nums or windowSize == 0:
        return []
    
    res = []
    window = deque()
    sl = SortedList()
    current_sum = 0.0 # 维护整个窗口 windowSize 的和
    
    # 目标：求 (sum(window) - sum(largest_k)) / (windowSize - k)
    
    for i in range(len(nums)):
        # 1. 进：新元素进入
        val = nums[i]
        window.append(val)
        sl.add(val)
        current_sum += val
        
        # 2. 出：旧元素滑出
        if len(window) > windowSize:
            old_val = window.popleft()
            current_sum -= old_val
            sl.remove(old_val)
        
        # 3. 算：窗口满了就开始算平均值
        if len(window) == windowSize:
            # 找到最大的 k 个数的和
            # 如果 k 不大，切片求和 O(k) 勉强能过
            # 如果 k 很大，面试官会要求 O(log W) 维护 top_k_sum
            largest_k_sum = sum(sl.islice(windowSize - k, windowSize))
            avg = (current_sum - largest_k_sum) / (windowSize - k)
            res.append(avg)
            
    return res