'''1852. Distinct Numbers in Each Subarray

You are given an integer array nums of length n and an integer k.
Your task is to find the number of distinct elements in every subarray of size k within nums.
Return an array ans such that ans[i] is the count of distinct elements in nums[i..(i + k - 1)] for each index 0 <= i < n - k.

 

Example 1:

Input: nums = [1,2,3,2,2,1,3], k = 3
Output: [3,2,2,2,3]
Explanation: The number of distinct elements in each subarray goes as follows:
- nums[0..2] = [1,2,3] so ans[0] = 3
- nums[1..3] = [2,3,2] so ans[1] = 2
- nums[2..4] = [3,2,2] so ans[2] = 2
- nums[3..5] = [2,2,1] so ans[3] = 2
- nums[4..6] = [2,1,3] so ans[4] = 3
Example 2:

Input: nums = [1,1,1,1,2,3,4], k = 4
Output: [1,2,3,4]
Explanation: The number of distinct elements in each subarray goes as follows:
- nums[0..3] = [1,1,1,1] so ans[0] = 1
- nums[1..4] = [1,1,1,2] so ans[1] = 2
- nums[2..5] = [1,1,2,3] so ans[2] = 3
- nums[3..6] = [1,2,3,4] so ans[3] = 4
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
'''
from collections import defaultdict;
from typing import List
def distinctNumbers(nums:List[int],k:int)->List[int]:
    res = []
    left = 0
    mini_dist = defaultdict(int)
    for right, num in enumerate(nums):
        mini_dist[num] += 1
        if right - left + 1 == k:
            cur_dist = len(mini_dist)
            res.append(cur_dist)
            mini_dist[nums[left]] -= 1
            if mini_dist[nums[left]] == 0:
                del mini_dist[nums[left]]
            left += 1
    return res

test = [1,2,3,2,2,1,3]
test_k = 3
print(distinctNumbers(test, test_k))

#reflected on 2024-06-10
#writing code on interveiw don't need to write the solution class
#remember to import the required modules
#