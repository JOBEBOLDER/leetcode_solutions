'''
Give a list of string, where every string in the list is of size 5.
Return the list of 5 string such that all the characters in each of the strings are unique
i.e if we combine all the strings(not nnecessary) we will have 25 unique characters)
eg
Input explanation
List of string with length of 5 each
intput = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "zabcd", "apple", "zebra", "ocean", "quick", "world", "jumps", "foxes", "liver"]

all the 5 string have unique character for both of the way
ouput = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"] or ["fghij", "klmno", "pqrst", "uvwxy", "zabcd"]

Got the intution of using with subsequence which will take TC : O(2^n)
Looking for optimal approach

abcde == bcdea	•	下面：过滤“不合法词” + 还把“等价词”（anagrams）合并掉
aabcd,

len(s) == 5:

chosen = []
possed=[]
backtracking(index, used_set, chosen):
#chooses
    -if it's unquie
    -append to the chossen
    -recursively chekc the next one
    -undo

#not choose

time:	M = 预处理后候选数量（M ≤ N，过滤掉重复字母、anagram 去重后）总时间：O(N + 2^M)（保守）或更“贴近题目结构”的：
O(N + M^5)（因为只选 5 个）

space:
	•	need_process + seen_set：O(M)
	•	递归栈深度最多 M：O(M)
	•	current_chosen 最多 5 个词、used_set 最多 25 个字母：O(1)（常数）

总空间：O(M)
'''

def find_five_words(strings):
    # --- 1. 预处理 (Pre-processing) ---
    # 过滤掉自身有重复字母的词（比如 "apple"），并去重（Anagrams）
    processed_words = []
    seen_sets = set()
    for s in strings:
        if len(set(s)) == 5:
            # 用 frozenset 作为 key 来识别字母组合相同的词
            char_set = frozenset(s)
            if char_set not in seen_sets:
                processed_words.append(s)
                seen_sets.add(char_set)

    ans = []
    n = len(processed_words)

    # --- 2. 回溯核心 (Backtracking) ---
    def backtrack(index, current_chosen, used_letters_set):
        # 成功条件：选够了 5 个词
        if len(current_chosen) == 5:
            # 注意：因为每次添加都检查了 isdisjoint，
            # 所以到达这里时，used_letters_set 必然包含 25 个唯一字母
            ans.append(list(current_chosen))
            return True # 返回 True 表示找到一个解就立即停止

        # 失败/终止条件
        if index >= n:
            return False

        # --- 剪枝优化 (Pruning) ---
        # 如果剩下的单词数加起来都不够 5 个，直接回溯
        if len(current_chosen) + (n - index) < 5:
            return False

        # --- 决策分支 ---
        
        # 分支 A: 尝试选择当前单词 processed_words[index]
        word = processed_words[index]
        word_set = set(word)
        
        # 检查冲突：当前单词的字母是否与已使用的字母重复
        if word_set.isdisjoint(used_letters_set):
            # 1. 做选择 (Do)
            current_chosen.append(word)
            used_letters_set.update(word_set)
            
            # 2. 递归 (Explore)
            if backtrack(index + 1, current_chosen, used_letters_set):
                return True # 找到解了，一路向上返回
                
            # 3. 撤销选择 (Undo / Backtrack)
            used_letters_set.difference_update(word_set)
            current_chosen.pop()

        # 分支 B: 跳过当前单词，直接看下一个
        if backtrack(index + 1, current_chosen, used_letters_set):
            return True

        return False

    # 执行回溯
    backtrack(0, [], set())
    return ans[0] if ans else []

# --- 测试 ---
input_strings = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "zabcd", "apple"]
print(find_five_words(input_strings))

# Example usage
strings = [
    "abcde", "fghij", "klmno", "pqrst", "uvwxy", 
    "axbyc", "fgtjk", "mnopq", "rstuv", "zzzzz"
]

result = find_unique_letter_strings(strings)
print("Selected strings:")
for res in result:
    print(res)


def find_word(strings:List[str]):
    #preprocessed:
    need_process = []
    seen_sets = set()
    for s in string:
        if len(set(s)) == 5:
            char_set = forzenset(s)
            if char_set not in seen_sets:
                need_process.append(s)
                seen_sets.add(char_set)
    
    n = len(need_process)
    #backtacking logic:
    def backtracking(index, chosen, used_set):
        #success conditon:
        if len(chosen) == 5:
            return chosen.copy()
        
        if index == n:
            return None
        
        word = need_process[index]
        cur_word_set = set(word)
        if cur_word_set.isdisjoint(used_set):
            chosen.append(word)
            used_set.update(cur_word_set)
            res = backtracking(index+1,chosen,used_set)
            if res:
                return res
            used_set.difference_update(cur_word_set)
            chosen.pop()
        return backtracking(index+1,chosen,used)
    return backtracking(0, [], set()) or []
            
'''
backtracking 返回的是：找到的解（list of 5 words）或者 None。
res 就是子递归的结果；如果它不是 None，就直接 return，把解往上层传。

'''