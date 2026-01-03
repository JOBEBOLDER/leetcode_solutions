'''
You are given a string containing only parentheses ('(' and ')') and digits (0-9). At the index of a digit, you must delete a number of 
parentheses to the left of the index equal to the digit's value. Return true if it is possible to balance the parenthesis of the input.

Example 1 Input: ((2)) Output: False Reason: Only possible string is unbalanced: "))"

Example 2 Input: ((((2)) Output: True Reason: Only possible string is balanced: "(())"

Example 3 Input: (()1(1)) Output: True Reason: Multiple possible strings and one is balanced: ")())", "(())", "()))".

Background: 

1.Digits should not be included in the result string, although that doesn't matter for calculating the boolean result.

2.If a digit doesn't have enough characters to the left to delete, then return false.



stack: [))] ->inbalance
[(())]->balance

time:On
space:On
'''

def checkbalance(self,s:str)->bool:
    #edge case:
    if not s:
        return False
    
    stack = []

    for i in range(len(s)):
        if s[i].isdigit():
            while stack:
                for j in range(len(int(s[i]))):
                    stack.pop()
        stack.append(s[i])

    #if len(left) == len(right):return true

    if stack:
        if stack.pop() == '(':
            left += 1
        elif stack.pop() == ')':
            right += 1

    return left == right