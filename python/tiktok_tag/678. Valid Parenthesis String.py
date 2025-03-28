class Solution:
    #space:2n
    #time:On,length of the chars
    def checkValidString(self, s: str) -> bool:

        left_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == '(':
                left_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            elif char == ')':
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        #for the rest chars:
        while left_stack and star_stack:
            if left_stack[-1] < star_stack[-1]:
                left_stack.pop()
                star_stack.pop()
            else:
                break

        return len(left_stack) == 0
        #✅ 所以只要所有 '(' 都被成功配对了，剩下多少 '*' 都没关系！
        #👉 left_stack 代表的是 没有配对成功的 '(' 左括号

        '''而我们允许：
            •	'*' 可以被当成 ')' 来匹配 '('
            •	'*' 也可以什么都不做（当作空）'''



                    