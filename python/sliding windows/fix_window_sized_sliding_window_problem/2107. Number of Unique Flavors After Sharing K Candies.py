'''
You are given a 0-indexed integer array candies, where candies[i] represents the flavor of the ith candy. 
Your mom wants you to share these candies with your little sister by giving her k consecutive candies, 
but you want to keep as many flavors of candies as possible.

Return the maximum number of unique flavors of candy you can keep after sharing with your sister.

 

Example 1:

Input: candies = [1,2,2,3,4,3], k = 3
Output: 3
Explanation: 
Give the candies in the range [1, 3] (inclusive) with flavors [2,2,3].
You can eat candies with flavors [1,4,3].
There are 3 unique flavors, so return 3.
Example 2:

Input: candies = [2,2,2,2,3,3], k = 2
Output: 2
Explanation: 
Give the candies in the range [3, 4] (inclusive) with flavors [2,3].
You can eat candies with flavors [2,2,2,3].
There are 2 unique flavors, so return 2.
Note that you can also share the candies with flavors [2,2] and eat the candies with flavors [2,2,3,3].
Example 3:

Input: candies = [2,4,5], k = 0
Output: 3
Explanation: 
You do not have to give any candies.
You can eat the candies with flavors [2,4,5].
There are 3 unique flavors, so return 3.
 

Constraints:

0 <= candies.length <= 105
1 <= candies[i] <= 105
0 <= k <= candies.length

'''
from collections import Counter
def shareCandies(candies: List[int], k: int) -> int:
        #base caseL
        if len(candies) < k or k < 0:
            return 0

        left = 0


        keep_count = Counter(candies)
        unique_keep = len(keep_count)
        res = float('-inf')

        if k == 0:
            return len(keep_count)

        for right,candy in enumerate(candies):
            keep_count[candy] -= 1
            if keep_count[candy] == 0:
                unique_keep -= 1

            if right - left + 1 > k:
                left_candy = candies[left]
                keep_count[left_candy] += 1
                if keep_count[left_candy] == 1:
                    unique_keep += 1
                left += 1
            if right-left+1 == k:
                res = max(res,unique_keep)

        return res

test_candies = [2,2,2,2,3,3]
test_k = 2
print(shareCandies(test_candies,test_k))
test_candies = [1,2,2,3,4,3]
test_k = 2
print(shareCandies(test_candies,test_k))

