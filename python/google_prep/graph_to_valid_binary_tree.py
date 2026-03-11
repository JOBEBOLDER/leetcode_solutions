'''
题目描述 (Original Problem Reconstruction)
Part 1: Graph to Valid Binary Tree
Problem Statement: 给定一个无向无环图（Undirected Acyclic Graph），
以邻接表 Map<Integer, List<Integer>> 的形式给出。请判断该图是否可以构成一棵合法的二叉树。

条件：如果能找到一个节点作为 root，使得所有节点的度数（degree）
满足二叉树条件（根节点最多 2 个子节点，其他节点最多 1 个父节点和 2 个子节点），则返回该 root；否则返回 -1 或报错。

Part 2: Color Consistency by Depth (Follow-up)
Problem Statement: 现在每个节点都有一个颜色属性（黑或白）。请判断是否存在一个 root，使得在该根节点确定的二叉树中，每一层（depth）的所有节点颜色都必须相同。

例如：第 0 层全是黑，第 1 层全是白，第 2 层全是白…… 这样是合法的。

'''


from collections import deque

def find_binary_tree_root(adj):
    nodes = list(adj.keys())
    n = len(nodes)
    
    # 遍历每一个可能的 root
    for root in nodes:
        # 1. 根节点在无向图中最多只能有 2 个邻居
        if len(adj[root]) > 2:
            continue
            
        # 2. 尝试从该 root 开始遍历
        visited = {root}
        queue = deque([root])
        is_binary = True
        
        while queue:
            curr = queue.popleft()
            
            # 统计子节点个数（除了父节点以外的邻居）
            children_count = 0
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    children_count += 1
                    queue.append(neighbor)
            
            # 3. 每个节点最多只能有 2 个子节点
            if children_count > 2:
                is_binary = False
                break
        
        # 4. 必须连通（访问到了所有节点）且符合二叉树结构
        if is_binary and len(visited) == n:
            return root
            
    return -1 # 找不到合法的 root

#第二问：
def find_colored_binary_tree_root(adj, colors):
    nodes = list(adj.keys())
    n = len(nodes)
    
    for root in nodes:
        if len(adj[root]) > 2:
            continue
            
        visited = {root}
        queue = deque([(root, 0)]) # 存储 (节点, 深度)
        depth_to_color = {}        # 存储 {深度: 颜色}
        is_valid = True
        
        while queue:
            curr, depth = queue.popleft()
            
            # --- Follow-up 核心逻辑：颜色检查 ---
            if depth not in depth_to_color:
                # 这一层还没见过，设置该层的“标准色”
                depth_to_color[depth] = colors[curr]
            else:
                # 这一层已有颜色，检查当前节点颜色是否一致
                if depth_to_color[depth] != colors[curr]:
                    is_valid = False
                    break
            
            # --- 结构检查 ---
            children_count = 0
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    children_count += 1
                    queue.append((neighbor, depth + 1))
            
            if children_count > 2:
                is_valid = False
                break
                
        if is_valid and len(visited) == n:
            return root
            
    return -1