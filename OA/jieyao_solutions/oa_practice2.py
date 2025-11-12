''''

你有一个嵌套的字典，存储了多个用户的活动记录，格式如下：

data = {
    "Alice": {"visits": [5, 3, 7], "country": "US"},
    "Bob": {"visits": [2, 8], "country": "UK"},
    "Carol": {"visits": [9], "country": "US"}
}

def summarize(data: dict, country_filter: str) -> dict:

output:
summarize(data, "US") 
# -> {"Alice": 15, "Carol": 9}
'''

def summarize(data: dict, country_filter: str) -> dict:
    result = {}
    for user,info in data.items():
        if info["country"] == country_filter:
            result[user] = sum(info["visits"])
            #key:user, value:the sum of the visits
    return result



'''
🧩 题 2：Simulate API Query (with Time Filter)

类型：字典 + 数据结构 + 时间复杂度分析

🧠 题目描述

你要实现一个简化版的 “metrics API”，能存储和查询时间序列数据。

编写类：
class MetricsStore:
    def __init__(self):
        ...
    def record(self, metric_name: str, timestamp: int, value: int) -> None:
        ...
    def query(self, metric_name: str, start: int, end: int) -> float:
        ...

        功能要求：
	1.	record(name, timestamp, value) 存储指标数据；
	2.	query(name, start, end) 返回 [start, end] 时间区间内该指标的平均值；
	3.	若指标不存在或无数据，返回 0；
	4.	要求查询复杂度 O(log n)（提示：排序 + 二分）。

store = MetricsStore()
store.record("cpu", 1, 40)
store.record("cpu", 2, 50)
store.record("cpu", 5, 70)

print(store.query("cpu", 1, 2))  # -> 45.0
print(store.query("cpu", 1, 5))  # -> 53.3
'''
# “I maintain a sorted list of (timestamp, value) per metric.
# Using binary search lets me locate the start and end range efficiently, keeping queries at O(log n + k).
# This mirrors how time-series databases handle range queries.”

import bisect import bisect_left,bisect_right
from collections import defaultdict

class MetricsStore:
    def __init__(self):
        self.data = defaultdict(list)
        
    def record(self,metric_name,timestamp,value):
        self.data[metric_name].append((timestamp,value))
        self.data[metric_name].sort() #keep sorted


    def query(self,metric_name,start, end):
        if metric_name not in self.data:
            return 0.0
        
        arr = self.data[metric_name]
        times = [t for t,_ in arr]
    # •	bisect_left(times, start)：找到 第一个 >= start 的时间的索引。
	# •	bisect_right(times, end)：找到 第一个 > end 的时间的索引。
        left = bisect_left(times,start)
        right = bisect_right(times,end)
        #如果区间内没有任何数据
        if left == right:
            return 0.0
        #👉 截取在时间区间 [start, end] 内的所有 (timestamp, value) 对应的值。
        vals = [v for _,v in arr[left:right]]
        return sum(vals) / len(vals)
    
'''
for example:
arr = [(1, 40), (2, 50), (5, 70)]
left = 0, right = 2
arr[left:right] = [(1, 40), (2, 50)]
vals = [40, 50]

步骤
操作
示例数据
1
拿到 metric 数据
[(1,40), (2,50), (5,70)]
2
提取时间戳
[1,2,5]
3
二分查找范围
[start,end]=[1,2] → left=0,right=2
4
切片取区间数据
arr[0:2]=[(1,40),(2,50)]
5
计算平均
(40+50)/2=45

'''

