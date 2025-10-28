import math
class Solution:

    '''
    understanding:
    input: string1,string 2
    output: string

    problem: 1.only upper case:
    2.Leet,code leetcode,codeleet

    match:
    i will use the counter: for example, 
    if string1+string2!=string2+string1 return ""

    in other case, we can use dictonary and stroe the occurances of each chars,
    string1 :ABCABC, so abc:all char appear 2 times,
    string2: ABC ,ABC:appear 1 times

    so the divisor we can just get the min_occocuances 

    def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    
    '''

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        g = math.gcd(len(str1), len(str2))
        return str1[:g]


        #