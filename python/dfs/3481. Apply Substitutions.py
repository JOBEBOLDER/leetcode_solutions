from typing import List
#time:O(n × m)
#space:O(n + m)
class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        # 构建替换映射
        mp = {k: v for k, v in replacements}
        memo = {}  # 记忆化展开结果
        visiting = set()  # 环检测
        
        def dfs(var: str) -> str:
            """递归展开变量的值"""
            # 如果变量不在映射中，返回原样（带$符号）
            if var not in mp:
                return f"%{var}%"
            
            # 如果已经计算过，直接返回结果
            if var in memo:
                return memo[var]
            
            # 如果正在访问中（检测到环），返回原样
            if var in visiting:
                # 注意：检测到环时不要存入memo，因为这不是最终结果
                return f"%{var}%"
            
            # 标记正在访问
            visiting.add(var)
            # 递归展开变量的值
            expanded = expand_value(mp[var])
            # 取消访问标记
            visiting.remove(var)
            
            # 只有成功展开（没有环）时才缓存结果
            memo[var] = expanded
            return expanded
        
        def expand_value(s: str) -> str:
            """展开字符串中的所有 $var$ 占位符"""
            result = []
            i = 0
            n = len(s)
            
            while i < n:
                if s[i] == '%':
                    # 寻找配对的 $
                    j = i + 1
                    # 找到下一个 $ 的位置
                    while j < n and s[j] != '%':
                        j += 1
                    
                    if j < n:  # 找到了配对的 $
                        var_name = s[i+1:j]
                        if var_name:  # 变量名不为空
                            # 递归展开这个变量
                            result.append(dfs(var_name))
                            i = j + 1  # 跳过整个 $var$
                        else:
                            # $$ 的情况，当作普通字符处理
                            result.append('%')
                            i += 1
                    else:
                        # 没有找到配对的 $，当作普通字符
                        result.append('%')
                        i += 1
                else:
                    # 普通字符，直接添加
                    result.append(s[i])
                    i += 1
            
            return ''.join(result)
        
        # 对输入文本进行展开
        return expand_value(text)