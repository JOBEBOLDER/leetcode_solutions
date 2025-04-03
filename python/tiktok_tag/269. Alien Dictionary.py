from collections import defaultdict, deque

class Solution:
    #time :O(N + K + E)
    #space:O(N + E)
    #拓扑排序其实就是把一个“有方向的图”（比如箭头 a → b → c）按照顺序排成一条线。
    '''思路总结：
    1:first we need to make a graph to define/represent all the words relationship
    2: use tropicial sort to output a line of the result'''

    def alienOrder(self, words):
        # 用邻接表表示图，比如 graph['a'] = ['b', 'c'] 表示 a -> b 和 a -> c
        #initialize the graph
        graph = defaultdict(list)

        # in_degree 记录每个字母的入度（有多少个字母指向它）
        in_degree = {}

        # 初始化 in_degree，确保每个字母都有一条记录（入度设为 0）
        for word in words:
            for char in word:
                if char not in in_degree:
                    in_degree[char] = 0

        # 遍历每对相邻的单词，找出它们的第一个不同字符，用来确定顺序
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # ⚠️ 检查非法情况：前面的单词比后面长，而且后面是前面的前缀
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            # 找出两个单词中第一个不同的字符
            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]
                if char1 != char2:
                    # char1 -> char2，表示 char1 应该在 char2 前面
                    if char2 not in graph[char1]:
                        graph[char1].append(char2)
                        in_degree[char2] += 1
                    break  # 只比较第一个不同的字符，后面不需要比了

        # 用队列来进行 BFS 拓扑排序
        queue = deque()

        # 把所有入度为 0 的字母放进队列，说明它们最先出现
        for char in in_degree:
            if in_degree[char] == 0:
                queue.append(char)

        result = ""

        # 开始拓扑排序
        #
        while queue:
            current_char = queue.popleft()
            result += current_char

            # 遍历 current_char 指向的所有字母
            for neighbor in graph[current_char]:
                in_degree[neighbor] -= 1  # 去掉 current_char 对 neighbor 的影响
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 如果结果里包含的字母数和 in_degree 的总数不一致，说明有环（非法）
        if len(result) != len(in_degree):
            return ""

        return result