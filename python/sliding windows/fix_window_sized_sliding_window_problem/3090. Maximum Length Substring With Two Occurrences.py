'''Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
'''
#so basicly the logic it's the repetition of each character can not more than2
#time:On
#space:On(n represent the number of the counter)
from collections import Counter
def maximumLengthSubstring(s:string)->int:
    left = 0
    ans = float('-inf')
    counter = Counter()

    for right,char in enumerate(s):
        counter[char] += 1
        while counter[char] > 2:
            left_char = s[left]
            counter[left_char] -= 1
            left += 1

        ans = max(ans,right-left+1)
    return ans

s1 = "aaaa" #2
s2 = "bcbbbcba" #4
print(maximumLengthSubstring(s1))
print(maximumLengthSubstring(s2))