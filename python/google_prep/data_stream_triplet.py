'''
Your task is to write a function that, given a distance d and a stream
of floating point values received one at a time, checks for groups of
three values within d distance of one another. Store the floating point values
in memory as they are received. When a group of three values meeting the
distance criteria is found, return the three values and remove them from the
memory.

面试官可能的口头复述（版本 A：最常见）

我们有一个实时数据流，每次会收到一个 float。给定一个距离阈值 d。
你需要在每次收到新值时，检查当前内存里是否存在三个值可以组成一个 triplet，使得它们两两之间的绝对差都小于 d。
也就是说对于 triplet (a, b, c)，要满足：
|a-b| < d、|a-c| < d、|b-c| < d。

一旦找到这样的一组三元组，就返回这三个值，并且把它们从内存结构中删除（因为它们已经被消费掉了）。
如果当前还找不到，就把这个新值也存起来，等待之后的数据。

你可以假设数据会持续到来，所以你实现一个像 add(value) 这样的接口，每次调用返回 None 或返回找到的 triplet。

✅ 总结每次调用

最坏情况下整体由插入、index、删除主导：

T(n) = O(n)

（常数很大，因为你做了多次线性操作。）

⸻

Space（空间复杂度）
	•	self.values 存下所有还没被组成 triplet 的值：最多 n 个 → O(n)
	•	其它临时变量（cluster 长度最多 3）→ O(1)

✅ 总结

S(n) = O(n)
'''

import bisect

class StreamProcessor:
    def __init__(self):
        self.values = []

    def check_values(self, new_value, d):
        # Insert the new value into the sorted list
        bisect.insort(self.values, new_value)

        # Find the index of the new value
        index = self.values.index(new_value)

        # Use a sliding window to find any clusters
        for i in range(index - 2, index + 1):
            if i >= 0 and i + 2 < len(self.values) and self.values[i + 2] - self.values[i] <= d:
                cluster = self.values[i:i + 3]
                # Remove the values from the list
                for v in cluster:
                    self.values.remove(v)
                return cluster

        return None

stream_processor = StreamProcessor()

# Test the function with some values
print(stream_processor.check_values(1.5, 1))  # None
print(stream_processor.check_values(2.0, 1))  # None
print(stream_processor.check_values(2.5, 1))  # [1.5, 2.0, 2.5]
print(stream_processor.check_values(3.0, 1))  # None
print(stream_processor.check_values(3.5, 1))  # None
print(stream_processor.check_values(4.0, 1))  # [3.0, 3.5, 4.0]


'''
maintain a sorted list of received values: As each new value is received, it is inserted into the correct position in the list to maintain the sorted order. This is done using a binary search algorithm, the time complexity of binary search is O(lgn), and if we use array to store the values, when we insert the value into the array, we need to move the values after the inserted index, the time complexity is O(n)
check for valid triplets: after inserting a new value, the algorithm checks for any triplets that include this new value and satisfy the condition. This is done by sliding a window of size 3 (for the triplet) across the list, centered around the position of the new value.
remove valid triplets: if a valid triplet is found, it is recorded and then removed from the list. This is done to prevent the same triplet from being recorded multiple times if another value is received that could also form a triplet with the same two other values.
The total time complexity is O(n)

如果你想展示高端技巧：先写出 bisect 版，然后跟面试官说：“如果数据量极大，我们可以用平衡搜索树或者哈希桶来优化到 $O(log N)$ 或 $O(1)$。”
'''

import bisect

class StreamProcessor:
    def __init__(self):
        self.values= []

    def find_triplet(self,new_val:int,dis:int):

        bisect.insort(self.values,new_val)
        index = self.values.index(new_val)

        for i in range(index - 2,index + 1):
            if i >= 0 and i + 2 < len(self.values) and self.values[i+2] - self.values[i] <= d:
                cluster = self.values[i:i+3]
                for v in cluster:
                    self.values.remove(v)
                return cluster
        return None
stream_processor = StreamProcessor()
print(stream_processor.find_triplet())


        