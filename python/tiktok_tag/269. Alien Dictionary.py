class Solution:
# time: O(N + E), where N = total characters, E = number of edges
# space: O(K + E), where K = number of unique letters
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = {}
        res = ""

        for word in words:
            for w in word:
                if w not in indegree:
                    indegree[w] = 0

        #build the graph:
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            if len(word1) > len(word2) and word1.startswith(word2):#wrfe->wrf
                return ""

            for j in range(min(len(word1),len(word2))):
                char1 = word1[j]
                char2 = word2[j]
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].append(char2)
                        indegree[char2] += 1
                    break

        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        while q:
            cur_char = q.popleft()
            res += cur_char
            for neighbour in graph[cur_char]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        return res if len(res) == len(indegree) else ""




