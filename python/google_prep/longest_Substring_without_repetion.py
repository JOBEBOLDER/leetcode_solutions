'''
s = "abcabcbb"
            ^ 
            ^
     map:{b:1,c:1,a:1}
     3max_window_size = max(current=1,max_window_size)

brute force: generate all the possible substring to see if they have repeat
time = On(n):n :length of the s
space:On,n:size of the mapping

'''
def longest_substring_without_repeat(s: str) -> int:
    #edge case:
    if s == '':
        return 0
    left = 0
    mapping = {}
    max_window_size = 0

    for right,char in enumerate(s):
        mapping[char] = mapping.get(char,0)+1
        while mapping[char] > 1:
            left_char = s[left]
            mapping[left_char] -= 1
            if mapping[left_char] == 0:
                del mapping[left_char]
            left += 1
        max_window_size = max(max_window_size,right - left + 1)
    return max_window_size
    
        
        

# debug your code below
print(longest_substring_without_repeat('abcdeffghij'))