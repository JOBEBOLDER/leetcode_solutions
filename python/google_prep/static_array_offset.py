'''
题目描述 (Original Problem Reconstruction)
Part 1: Static Array (热身)Problem Statement:
给定一个数组 arr 和一个整数 offset。如果 offset > 0，
返回数组的前 offset 个元素。如果 offset < 0，返回数组的最后 abs(offset) 个元素。注：
如果 abs(offset) 超过数组长度，则根据具体沟通返回全部。

Part 2: Streaming Data (核心)
Problem Statement:现在数组不再是静态的，而是一个数据流（Stream）。
你无法直接获取数组长度，只能通过两个方法与流交互：hasNext(): 
返回布尔值，表示是否有下一个元素。getNext(): 返回流中的下一个元素。
Challenge:在 offset 为负数的情况下（即需要获取最后 $N$ 个元素），
由于你不知道流什么时候结束，你该如何高效地保留最后 $N$ 个元素，且空间复杂度最优？

'''

def get_elements_static(arr, offset):
    if offset == 0:
        return []
    if offset > 0:
        return arr[:offset]
    else: # offset < 0
        return arr[offset:] # Python 负索引自带“倒数”功能
    

from collections import deque

def get_elements_stream(stream, offset):
    if offset == 0:
        return []

    # 情况 A: 正数 offset (非常简单，直接取前 N 个)
    if offset > 0:
        result = []
        count = 0
        while stream.hasNext() and count < offset:
            result.append(stream.getNext())
            count += 1
        return result

    # 情况 B: 负数 offset (核心考察点)
    # 我们需要知道最后 N 个，所以要维护一个长度为 k 的队列
    else:
        k = abs(offset)
        # 使用 deque (双端队列) 模拟固定长度窗口
        window = deque()
        
        while stream.hasNext():
            window.append(stream.getNext())
            # 如果队列超过了 k，就把最老的元素踢掉
            if len(window) > k:
                window.popleft()
        
        return list(window)
    
'''
设数组长度 n，流长度 m，k = abs(offset)。
	•	静态数组：
	•	Time = O(min(|offset|, n))
	•	Space = O(min(|offset|, n))（切片会拷贝输出）
	•	数据流 offset > 0（取前 offset 个）：
	•	Time = O(min(m, offset))
	•	Space = O(min(m, offset))
	•	数据流 offset < 0（取最后 k 个）：
	•	Time = O(m)（必须读完整个流）
	•	Space = O(k)（固定窗口存最后 k 个，最优）


'''

def get_offset(self,arr,offset:int): #offset:positive/negative
    if offset == 0:
        return []
    if offset > 0:
        return arr[:offset]
    if offset < 0:
        return arr[offset:]
    

#if the data stream is dynamic:

def get_element_dynamic(self,data_stram,offset):
    if offset == 0:
        return []
    #if the offset > 0
    if offset > 0:
        count = 0
        res = []
        while data_stram.hasNext() and count < offset:
            res.append(data_stram.getNext())
            count += 1

    #if the offset < 0
    if offset < 0:
        window = deque() #double queue
        res = []

        k = abs(offset)
        while data_stram.hasNext():
            window.append(data_stram.getNext())
            if len(window) > k:
                window.popleft()
        return list(window)

    0
1       2

adj:dict:{
    0:[1,2]
    1:[]
    2:[]
}

def validate_binary_tree(adj):
    nodes = list(adj.keys())
    n = len(nodes)

    for node in nodes:
        #root should only has 1 child :one indegree
        # 这个候选 root 一看就不可能（根最多 2 个孩子）→ 跳过
        if len(adj[node]) > 2:
            continue

        #i found the root, and start travsering from there
        visited = set()
        queue = deque()
        queue.append(node)
        visited.add(node)
        is_binary = False

        while queue: #[0]
            cur = queue.popleft() #cur = 0
            child_count = 0
            for nei in adj[cur]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
                    child_count += 1
            if child_count > 2:
                is_binary = True
                break
        if is_binary and len(visited) == n:
            return root
    return -1
            


