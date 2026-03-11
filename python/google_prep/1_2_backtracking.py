'''
第三轮 只用1和2组合出N，print出所有可能的组合 ✅ 第三轮 只用1和2组合出N，print出所有可能的组合 ✅ 

举例： 4 → 1 1 1 1; 1 1 2; 1 2 1; 2 1 1; 2 2

backtracing(remainging,path)
#endcondtion
remainging == 0

path.append(1)
backtracing(remaining - 1,path)
path.pop()

path.append(2)


这个呢
'''

def print_combinations(n):
    # path 用来记录当前的组合
    def backtrack(remaining, path):
        # 终止条件：正好凑够 N
        if remaining == 0:
            print(" ".join(map(str, path)))
            return
        
        # 剪枝：如果剩余值小于 0，说明此路不通
        if remaining < 0:
            return
        
        # 尝试放 1
        path.append(1)
        backtrack(remaining - 1, path)
        path.pop() # 回溯：撤销选择
        
        # 尝试放 2
        path.append(2)
        backtrack(remaining - 2, path)
        path.pop() # 回溯：撤销选择

    backtrack(n, [])

# 测试
# print_combinations(4)