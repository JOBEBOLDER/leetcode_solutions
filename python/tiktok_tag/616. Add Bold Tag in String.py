class Solution:
    '''
    Time: O(n * k)
    Space: O(n)
    '''
    def addBoldTag(self, s: str, words: List[str]) -> str:
        status = [False] * len(s)
        final = ""

        for word in words:
            start = s.find(word)

            last = len(word)

            while start != -1:
                for i in range(start, last + start):
                    status[i] = True
                start = s.find(word, start + 1) #找到一个find的index，继续找下一个

        i = 0
        while i < len(s):
            if status[i]:
                final += '<b>'
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += '</b>'
            else:
                final += s[i]
                i+=1

        return final