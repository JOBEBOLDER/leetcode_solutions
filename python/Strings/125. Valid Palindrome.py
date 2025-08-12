'''
understand:
input:
s = "A man, a plan, a canal: Panama"
output:boolean

logic:
detemine that this should be palindrome:

questions:
- what if the string =empty? -> true
- what if only one char -> also consider true
- do the string have special characters? *#%&?
- do we inclued upper case and also lower case? -> need to convert to all lower case
- do have have empty space" "? ->yes, and we need to excluded it


match & plan:
- two pinters
plan:
- first to convert the s-> lowercase and also connect together make it a string without " "
- we can do 2 pointer here, left:start , right:end
-do a while loop,stop condition:when left pointer exceed right pointer:
    - check if s[left] != s[right]:
            - return False
        left += 1
        right -= 1

    return true

so this is basiclly my plan, does my plan sounds good to you?
shoudl i implement it?

time:On
space:On(n->length of the string)
'''

#implementation:

def isPalindrome(s: str) -> bool:
    sb = []

    for c in s:
        if c.isalnum():
            sb.append(c.lower())

    #excluded the empty space:
    word = "".join(sb)

    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1

    return True


#test cases:
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
s = "race a car"
print(isPalindrome(s))



