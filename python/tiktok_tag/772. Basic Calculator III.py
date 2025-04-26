class Solution:
    #time:On
    #space:On
    def calculate(self, s: str) -> int:
        startIndex = {}
        stack = []
        #忘记了用stack依次处理（的索引
        for i in range(len(s)):
            if s[i] == '(':
               stack.append(i)
            elif s[i] == ')':
                startIndex[stack.pop()] = i
        return self.calculate_helper(s,0,len(s) - 1,startIndex)


    def calculate_helper(self,s:str,start:int,end:int,startIndex):

        stack = []
        sign = '+'
        num = 0

        i = start

        while i <= end:
            #记得分情况处理，
            char = s[i]
            if char.isdigit():
                num = num *10 + int(char)

            if char == '(':
                num = self.calculate_helper(s,i + 1, startIndex[i] - 1,startIndex)
                i = startIndex[i]

            if char in '+-*/' or i == end:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = char
                num = 0
            i += 1

        return sum(stack) if stack else -1

        

