'''
1. 题目还原：Pi 序列索引匹配 (Pi Index Match)题目描述：给定一个表示圆周率 $\pi$（或任意长数字）的字符串 pi。
你需要找到所有满足“索引值 $i$ 等于该索引处数字”的 $i$。1-based Index：索引从 1 开始计算。
匹配规则：对于个位数索引（如 $i=3$），只需满足 pi[i-1] == '3'。对于多位数索引（如 $i=456$），
要求该索引对应的数值字符串整体出现在 pi 的相应位置。具体来说，如果 $i$ 是一个 $k$ 位数，那么从 pi 的第 $i - k$ 个位置开始（以 0 为起始），

接下来的 $k$ 个字符必须正好组成数字 $i$。示例：pi = "31415"$i=1$: pi[0] 是 '3'，不匹配。$i=3$: pi[2] 是 '4'，不匹配。多位示例：
若 $i=456$（长度为 3），则需要检查：
pi[456-3] 即 pi[453] 是否等于 '4'
pi[456-2] 即 pi[454] 是否等于 '5'
pi[456-1] 即 pi[455] 是否等于 '6'

return :List[pi_match_index_elements]

'''

def find_pi_match(pi:str):
    #edge cases:
    if not pi:
        return []
    
    res = []
    n = len(pi)

    for i in range(1,n+1):
        str_i = str(i)
        length = len(str_i) ## i=456, length=3, need pi[453:456]
        start_index = i - length

        if start_index >= 0 and pi[start_index:i] == str_i:
            res.append(i)

    return res
