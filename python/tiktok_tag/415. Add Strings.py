class Solution:
    #time:On+M
    #space:O1
    #strings in Python are immutable.
    #Lists in Python are mutable,
    '''Whenever you’re building a string piece by piece in a loop, especially from the back or in reverse, think:

    “Am I adding many characters over time? Is performance important?”
'''
    def addStrings(self, num1: str, num2: str) -> str:
        result = [] #initialize the result

        #we need to consider :carry, digits

        #two pointers:
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0


        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i >= 0 else 0 #handle the case where either one string are empty string
            y = int(num2[j]) if j >= 0 else 0

            cur_sum = x + y + carry

            #handle the carry for next round calculation and also the digit:
            carry = cur_sum // 10
            digit = cur_sum % 10

            result.append(str(digit))

            i -= 1
            j -= 1

        return "".join(result[::-1])

