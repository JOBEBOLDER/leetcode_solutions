'''
understand:
input:s = 2 strings
output: string

logic:
minimum window substring of s such 
that every character in t (including duplicates) is included in the window.

quesitons:
-empty s or empty t?
- len(t) > len(s) -> return false
- no special characters
- consist upper and lower

match& plan:
maybe sliding window?->calculate the length of the window

plan:
use sliding window,
2 counter
2pointers:set left = -1,right = the last element
find the smaller window if exist,update the window size
otherwise keep shrinking to find the smaller one

'''
from collections import Counter
def minWindow(s: str, t: str) -> str:
    #base case check:
    if len(t) > len(s):
        return ""
    
    #initialization of the 2 counters:
    counter1 = Counter()
    counter2 = Counter(t)

    # #	•	ans_left = -1：方便用负数来判断“没找到”。
	# •	ans_right = len(s)：和 -1 配合制造一个“比任何可能解都大的长度”，保证第一次就能更新。
    left = 0
    ans_left = -1
    ans_right = len(s)

    #‼️记得
    for right,char in enumerate(s):
        counter1[char] += 1

        while counter1 >= counter2:
            if right - left < ans_right - ans_left:
                ans_left = left
                ans_right = right
            counter1[s[left]] -= 1
            left += 1
    return "" if ans_left == -1 else s[ans_left:ans_right + 1]

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))

s = "a"
t = "a"
print(minWindow(s,t))

s = "a"
t = "aa"
print(minWindow(s,t))






