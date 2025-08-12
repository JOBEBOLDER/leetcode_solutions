'''
understand:
input: string1,string2
output:boolean

logic: return true if one of s1's permutations is the substring of s2.
and the order is not matter

questions:
this is the base case and constrants that i can think of right now:
- what if wither one is empty:string1/s2?->return false
- s1:ab, s2:Ab:lowercase/upper matter? only lower
- empty string in the middle?

match& plan:
sliding window?

plan:
iterate s1,s2->make 2 hash table, and compare 2 hashtable frenquenices 
s2 should have same freq with s1
use 26 arrays:


'''
def checkInclusion(s1:str,s2:str):
    n = len(s1)
    m = len(s2)
    #base case check:
    if n > m:
        return False

    base = ord('a')

    freq1 = [0] * 26

    for i in range(n):
        freq1[ord(s1[i]) - base]+= 1

    freq2 = [0] * 26
    for i in range(m):
        freq2[ord(s2[i]) - base]+= 1
        if i >= n:
            #其实比较的是freq1 ,freq2
            freq2[ord(s2[i - n]) - base] -= 1
            # 比较两个频次数组
            if freq2 == freq1:
                return True

    return False

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1,s2))