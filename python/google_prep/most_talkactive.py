'''
There's this text log file (single file) that contains a chat transcript of a chat room (can have multiple people talking).
Something like the following -

10:00 <alice> Hi! What's up?
10:01 <bob> Hey
10:03 <alice> Dinner?
10:04 <john> I'm down! But only if it isn't vegan.
.
.
.... could be more entries

You have to parse this file. And store data into a DS of your choice. Furthermore, 
we want to know the top n number of most talkative people. You would return that in a DS of your choice again,
 which must contain the top n people's usernames and the number of words they have typed out per the transcript.


 # **面试里要主动澄清的点（加分）**

你可以在开头快速问一句：

1. “是按**消息条数**算 talkative，还是按**字符数**/单词数？”
2. “如果 topK 有并列，要怎么 tie-break？我默认按 username 字典序。”
3. “不合法行是跳过还是报错？我先跳过。”
'''

import re
import heapq
from collections import defaultdict
from typing import List, Tuple, Optional, DefaultDict

class ChatAnalyzer:
    def __init__(self):
        # 匹配格式: HH:MM <username> text...
        self.pattern = re.compile(r'^[\d:]+\s+<(\w+)>\s+(.*)$')

    def get_top_talkative_users(self, file_path: str, n: int) -> List[Tuple[str, int]]:
        """
        解析聊天记录并返回字数最多的前 n 个人。
        返回格式: [(username, total_word_count), ...]
        """
        # defaultdict(int) -> 默认 0，累加更省事
        word_counts: DefaultDict[str, int] = defaultdict(int)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    parsed = self._parse_line(line)
                    if not parsed:
                        continue

                    user, text = parsed
                    word_counts[user] += len(text.split())

        except IOError as e:
            print(f"Error reading file: {e}")
            return []

        # top n by word count
        return heapq.nlargest(n, word_counts.items(), key=lambda item: item[1])

    def _parse_line(self, line: str) -> Optional[Tuple[str, str]]:
        """
        解析单行数据，合法则返回 (username, content)，否则返回 None
        """
        match = self.pattern.match(line.strip())
        if not match:
            return None
        return match.group(1), match.group(2)


if __name__ == "__main__":
    analyzer = ChatAnalyzer()
    # result = analyzer.get_top_talkative_users('chat.txt', 3)
    # print(result)



class analyze:
    def __init__(self):
        self.pattern.compile()

    def get_most_talkactive_user(self,file_path:str, n:int)->List[Tuple[str,int]]:
        word_counts:DefaultDict[str,int] = defaultdict(int)

        try:
            with open(file_path,'r',encoding='utf-8') as file:
                for line in file:
                    parsed = self.parsed(line)
                    if not parsed:
                        continue
                    user,text = parsed
                    word_counts[user] += len(text.split())
            #word_counts.items() = [("alice", 12), ("bob", 5), ("john", 20)]
            return heapq.nlargest(n,word_counts.items,key=lambda item:item[1])


        except IOError as e:
            print(f"can not open file due to {e}")


    def parsed(self, line:str)->optional[Tuple[str,str]]:
        match = self.pattern.match(line.strip())
        if not match:
            return None
        return match.group(1),match.group(2)
