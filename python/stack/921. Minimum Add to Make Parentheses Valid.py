class Solution:
    #time:On
    #space:O1
    def minAddToMakeValid(self, s: str) -> int:
        close_need = 0
        open_need = 0

        for i in range(len(s)):
            if s[i] == '(':
                close_need += 1

            elif s[i] == ')':
                if close_need > 0:
                    close_need -= 1
                    #如果 close_need == 0，说明没有多余的 '(' 可以匹配，那只能补一个 '(' → open_need += 1
                elif close_need == 0:
                    open_need += 1

        return open_need+close_need