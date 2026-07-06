from collections import Counter

from typing import List
class Solution:
    def majorityElement(self,nums:List[int])->int:
        count = Counter(nums)
        max_value = max(counter.values())

        for k,value in counter.items():
            if value == max_value:
                return k
            
#time: O(n) time
#space: O(1) space 