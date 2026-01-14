'''
input: nums array[int]
output: list[int]

freq: more than n/3
3:2
2:1
n == 3,3/3 = 1


pq[()]
'''
import heapq
'''
	•	建 Counter(nums)：O(n)
	•	把所有不同元素（记为 k 个）都 push 进 heap：O(k log k)
	•	再全部 pop：O(k log k)
	•	总体：O(n + k log k)
最坏 k = n → O(n log n)（不是 n log n 必然，但最坏是）

空间：Counter + heap 都是 O(k)，最坏 O(n) ✅

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        pq = []
        time = n / 3
        for num ,freq in counter.items():
            heapq.heappush(pq,(freq,num))

        res = []
        while pq :
            freq,num = heapq.heappop(pq)
            if freq > time:
                res.append(num)
        return res

'''
optional solution:
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for key in count:
            if count[key] > len(nums) // 3:
                res.append(key)

        return res


'''