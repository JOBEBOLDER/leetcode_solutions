def make_combination(n):
    def backtracking(remain, path):
        #end condtion:
        if remain == 0:
            print("".join(map(str,path)))

        #pruning:
        if remain < 0:
            return
        
        path.append(1)
        backtracking(remain - 1,path)
        path.pop()


        path.append(2)
        backtracking(remain - 2, path)
        path.pop()

    backtracking(n,[])
    return -1


'''
queue:deque([sorces])
visited = set()
while queue:
    socrece == destineation
    return True

    #check all of the nei

'''
def reachable(routers:List[Tuple[int,int]],r: float, sources:int, destination:int) -> bool:
    length = len(routers) #we van get the index of all the routers
    visited = [False] * n
    queue = deque([sources])

    while queue:
        u = queue.popleft()
        x1,y1 = routers[u]
        for v in range(n):
            if not visited[v]:
                x2,y2 = routers[v]
                dx,dy = x1-x2,y1-y2
                if dx*dx + dy*dy <= r:
                    if v == destination:
                        return True
                    visited[v] = True
                    queue.append(v)
    return False

    0
 1       1
0 1

# number of island: connected component
'''
dfs()

preorder
node.val == 1, parent.val == 0

#recursively traver the left and rigth subtree

'''
class TreeNode:
    def __init__(self,left=None,right=None,val = 0):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #find the entrance
    #sink the island
    def find_island_on_tree(root:Optional[TreeNode]):

        island_number = 0

        def dfs(node,parent): 
            nonlocal island_number
            if not root:
                return 
            
            if node.val == 1 and parent.val == 0:
                island_number += 1

            dfs(node.left,node.val)
            dfs(node.right,node.val)

        dfs(root,0)
        return island_number
    

    # Follow-up: Count the sizes of each island.
    def count_island_size(root):
        size = []

        def traverse(root):
            if not root:
                return 
            if root.val == 1:
                # 发现岛入口 -> 立刻去吃掉整座岛并数面积，traverse = scan every node, once you see a 1, 
                # that must be a new island (because we will sink islands), so start a DFS to consume it.
                size.append(self.dfs(root))

            traverse(root.left)
            traverse(root.right)

        # dfs 做什么？——“沉岛 + 数面积”
        def dfs(root):
            if not root or root.val == 0:
                return 0
            
            root.val = 0

            return 1 + dfs(root.left) + dfs(root.right)

  # #dfs(node) returns the size of the 1-component connected to this node.
# If node is water (0) or null → size 0.
# Otherwise count itself (1), mark it visited (set to 0), then add sizes from children.      



def find_five_word(strings:List[str])-> List[str]:
    #pre-processed:
    #abcde == edcba
    need_process = []
    seen_set = ()
    for string in strings:
        if len(set(string)) == 5:
            char_set= frozenset(string)
            if char_set not in seen_set:
                need_process.append(string)
                seen_set.add(char_set)

    res = []
    n = len(need_process)
    #backtracking:
    def backtracking(index, current_chosen, used_set):
        #end condtion:
        if len(current_chosen) == 5:
            res.append(list(current_chosen))
            return True
        #optimazation : pruning:
        if index >= n:
            return False
        
        if len(current_chosen) + n - index < 5:
            return False
        
        #do backtracking:
        word = need_process[index]
        word_set = set(word)

        if word_set is disjoint(used_set):
            current_chosen.append(word)
            used_set.update(word_set)

            if backtracking(index+1,current_chosen,used_set):
                return True #is help us to stop the backtracking once we found the target
            current_chosen.pop()
            used_set.difference_date(word_set)

        #not chossing:
        if backtracking(index+1,current_chosen,used_set):
            return True
        
    ok = backtracking(0,[],set())
    return res if ok else []

'''
queue =[]:k size of the window
cur_sum + num
popleft :cursum - num

x largetest element in the K window
sorted list = [:x]




'''     
class calculateAverage:
    def __init__(self,k:int,x:int):
        self.k = k
        self.x = x
        self.sl = SortedList()
        self.queue = deque()
        self.cur_sum = 0

    def add(self,val:int):
        self.queue.append(val)
        self.cur_sum += val
        self.sl.add(val)

        if len(self.queue) > self.k:
            removed = self.queue.popleft()
            self.cur_sum -= removed
            self.sl.remove(removed)

        #你的 k 是窗口大小（windowSize）。你每次 add_element 只往窗口里加一个数；在刚开始的前 k-1 次调用里，窗口元素个数 < k，
        # 还没有形成一个完整窗口，所以你选择返回 0.0（也可以选择返回 None 或不返回结果，取决于题目要求）。
        if len(self.queue) < self.k:
            return 0.0

        actual_x = min(self.x,len(self.sl))
        cur_sum = sum(self.sl[-actual_x:]) if actual_x > 0 else 0
        trimmed_sum = self.cur_sum - cur_sum
        trimmed_length = self.k - actual_x
        avg = trimmed_sum // trimmed_length

        return avg if avg > 0 else 0.0

import re
import heapq
#most talk active:
class Analyze_talking:
    def __init__(self):
        self.pattern = re.compile()

    def get_top_k_talkactive(self,file_path:str,k:int):
        count = DefaultDict[str,int] = defaultdict(int)

        try:
            with open(file_path ,"r","utf-8") as file:
                for line in file:
                    parsed = self.parse(line)
                    if not parsed:
                        continue
                    user,text = parsed
                    count[user] += len(text.split())
                
    
        except IOError as e:
            print(f"file is invalid becuase of{e}")
            return []
        
        return heapq.nlargest(n,count.items(), key=lambda item:item[1])



    def parse(self,lines:str)->Optional[Tuple[str,str]]: #username: text 
        match = self.pattern.match(line.strip())
        if not match:
            return None
        return match.group(1), match.group(2)



class RestaurantWaitingList:
    def __init__(self):
        self.waitlist = []


    def join_waitlist(self,party_name,party_size):
        for name,size in self.waitlist:
            if name == party_name:
                print(f"{party_name} already in the waiting list")
            self.waitlist.append((party_name,party_size))
            print(f"{party_name} with {party_size} already successfully joined the waitlist")


    def leave_waitlist(self,party_name):
        for entry in self.waitlist:
            if entry[0] == party_name:
                self.waitlist.remove(entry)
                print(f"{party_name} removed successfully on the waiting list")
                return 
        print(f"{party_name} can not find on the waiting list")
            

    def show_waitlist(self):
        if not self.waitlist:
            print("the waiting list is empty right now")
        print("current waiting list:")
        for name ,size in self.waitlist:
            print(f" - party {name} of size {size}")


    def serve_customer(self,table_size):
        for entry in self.waitlist:
            party_name,party_size = entry
            if party_size == table_size:
                self.waitlist.remove(entry)
            print(f"successfully served {party_name}")
            return
        print(f"can not find the size of {table_size} right now")


def can_form_master_sequence(subsequences:List[List[int]])->bool:
    #buidl a graph:
    adj = defaultdict(set)
    nodes = set()
    indegree = defaultdict(int)

    for sub in subsequences:
        for i in range(len(sub)):
            nodes.add(sub[i])
            if i > 0:
                u,v = sub[i-1],sub[i]
                adj[u].add(v)
                indegree[v] += 1

    queue = deque()
    for node in nodes:
        if indegree[node] == 0:
            queue.append(node)

    visited = 0
    while queue:
        cur = queue.popleft()
        visited += 1

        for nei in adj[cur]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    return visited == len(nodes)


def find_taxi_distance(grid):
    m = len(grid)
    n = len(grid[0])

    dis = [[float('inf') * n for _ in range(m)]]

    queue = deque()
    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'T':
                queue.append((i,j))
                dis[i][j] = 0

            elif grid[i][j] == 'W':
                dis[i][j] = -1

    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            nx ,ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '0' and dis[nx][ny] == float('inf'):
                dis[nx][ny] = dis[x][y] + 1
                queue.append((nx,ny))
    return dist

def min_cut_to_disconnect_with_uni_directional(edges):
    adj = defaultdict(list)
    weights = {}
    for parent,child,w in edges:
        adj[parent].append(child)
        weights[(parent,child)] = w

    def dfs(node,parent):
        #not the root
        if parent != -1:
            cut_cost = weights[(parent,node)]
        else:
            cut_cost = float('inf')

        is_leaf = len(adj[node]) == 0
        cut_child_cost = 0
        #two cases: to cut the child recersively:
        for child in adj[node]:
            cut_child_cost += dfs(child,node)
        return min(cut_child_cost,cut_cost) if not is_leaf else cut_cost


def group_buddies(stirngs:List[str])->List[str]:
    groups = defaultdict(list)


    for string in strings:
        if string == "":
            groups[("")].append(string)

        if len(string) == 1:
            groups[("length1")].append(string)


        feature = [] #secreat code [101]
        # Feature Sequence)
        for i in range(1,len(string)):
            diff = (ord[i] - ord[i-1]) % 26
            feature.append(diff)
        groups[(feature)].append(string)

    return list(groups.values())
        



























