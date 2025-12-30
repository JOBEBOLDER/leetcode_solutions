'''
Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
Constraints:

[time limit] 5000ms

[input] array.character arr

1 ≤ arr.length ≤ 30
[input] string str

1 ≤ str.length ≤ 500
[output] string


'''

from typing import List
'''
problem statement:
intput: arr =[] unique
str:""

return string:  smallest substring of str containing all the characters in arr

edge cases:
return "" if we can not find the subtring

- either arr or string:empty
if arr is empty:->return emtpy""
if string is empty->return empty""

sliding windows: 
arr = ['x','y','z']
map:{x:1,y:1,z:1} set = len(arr) = 3:required = 3
currentwindowsize = 0,if curr_window < best: best_start=slow,best : fast-slow + 1
arr = set(arr),
form = 3
xyyzyzyx
       ^
 ^

'''

def get_shortest_unique_substring(arr: List[str], s: str) -> str:
    #the end condtion both reach to the end
    #edge cases:
    if len(s) < len(arr):
      return ""
    fast = 0
    slow = 0
    arr_set = set(arr)
    mapping={}
    
    formed = 0
    required = len(arr_set)
    best_len = float('inf')
    best_start = 0

    #begin to add the element into the window:
    for fast in range(len(s)):
      ch = s[fast]
      if ch in arr_set:
        mapping[ch] = mapping.get(ch,0)+1
        if mapping[ch] == 1:
          formed += 1

      #shrink the window when needed:when we have every char we need in set
      while formed == required:
        #calculate the size first
        cur_len = fast - slow + 1
        if cur_len < best_len:
          best_start = slow
          best_len = cur_len

        char2 = s[slow]
        #因为我们只关心 arr 里那些“必须包含”的字符；窗口左边丢掉一个“不需要的字符”并不会让窗口失效，也不应该影响 formed。
        if char2 in arr_set:
          mapping[char2] -= 1
          if mapping[char2] == 0:
            formed -= 1
          
        slow += 1

    return "" if best_len == float('inf') else s[best_start:best_start + best_len]




    



