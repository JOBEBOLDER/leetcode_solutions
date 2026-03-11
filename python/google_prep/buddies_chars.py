'''
1. 题目解析 (English Reconstruction)Title: Group Strings by 
Character Distances (Buddies)Problem Statement:Given a list of strings, 
group them if they are "buddies."
Two strings are buddies if:They have the same length.
The distance between corresponding characters is the same.
Examples:"aaa" and "bbb":"aaa": 
distances are a-a=0, a-a=0 $\rightarrow$ (0, 0)"bbb":
 distances are b-b=0, b-b=0 $\rightarrow$ (0, 0)

Result: Buddies."abc" and "zab":"abc": b-a=1, c-b=1 $\rightarrow$ (1, 1)"zab": 
a-z=1 (circularly, z $\rightarrow$ a is 1), b-a=1 $\rightarrow$ (1, 1)Result: Buddies.
'''



from collections import defaultdict
from typing import List

def group_buddies(strings: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    
    for s in strings:
        # 1. 基础情况：空字符串或长度为 1
        if not s:
            groups[("",)].append(s)
            continue
        if len(s) == 1:
            groups[("len1",)].append(s)
            continue
            
        # 2. 计算特征序列 (Feature Sequence)
        # 计算相邻字符的相对距离
        feature = []
        for i in range(1, len(s)):
            # (后一个 - 前一个) % 26 确保了 z->a 的距离是 1
            diff = (ord(s[i]) - ord(s[i-1])) % 26
            feature.append(diff)
            
        # 3. 将序列作为 Key (Tuple 是可哈希的)
        # 别忘了加上长度，防止不同长度但差值序列相同的巧合（虽然在这个逻辑下长度已经隐含了）
        groups[tuple(feature)].append(s)
        
    return list(groups.values())

# --- 测试 ---
# input = ["aaa", "bbb", "abc", "zab", "az", "ba", "a"]
# print(group_buddies(input))

def group_buddies(self,strings:List[str])->List[List[str]]:
    groups = defaultdict(list)

    for s in strings:
        if not s:
            groups[("",)].append(s)
        if len(s) == 1:
            groups[("len1",)].append(s)

        feature = []
        for i in range(1,len(s)):
            diff = (ord[i] - ord[i-1]) % 26
            feature.append(diff)

        groups[tuple(feature)].append(s)

    return list(groups.values())
