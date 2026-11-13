'''You are given a binary array nums, *you should delete one element from it*.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''
from collections import Counter
def longestSubarray(nums:List[int])->int:
    #edge case:
    if not nums:
        return 0
    #initialize the variables:
    left = 0
    ans = float('-inf')
    counter = Counter()
    

    #sliding windows,expand the window while still valid, and shrink the window when is not, and also remove the elements in the window
    for right,num in enumerate(nums):
        if num == 0:
            counter[0] += 1
        while counter[0] > 1:
            left_one = nums[left]
            if left_one == 0:
                counter[left_one] -= 1
            left += 1
        ans = max(ans,right-left+1-1) #right-left+1-1,the reason why -1 it's becasue we are removing one element from the array
    return ans

test_nums = [0,1,1,1,0,1,1,0,1]
test_nums_1 = [1,1,0,1]
test_nums_2 = [1,1,1]
print(longestSubarray(test_nums))
print(longestSubarray(test_nums_1))
print(longestSubarray(test_nums_2))