class Solution:
    '''
    understand:
    input:nums1,nums2,array,they are increasing order
    output:the nested list of the pre_k minsum list

    some hit:
        k pairs:using heap
        ❗ 我们不是只操作堆一次

    ② 主循环

    我们最多取 k 个 pair，所以：
        •	k 次 heappop → 每次 log(k)
        •	k 次 heappush → 每次 log(k)
    堆操作时间是 log(heap_size)

    → 总是 O(k log k)

    ③ 结果数组 res

    res 大小就是 k
    → O(k)

    
    
    
    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #base case:
        if not nums1 or not nums2 or not k:
            return []

        #initialization:
        res = []
        heap = []
        m = len(nums1)
        n = len(nums2)

        #只用关注前k个，但是不保证m比k小，所以是min(m,k)
        ## 初始化：固定 j = 0，把 (i, 0) 这条“纵向链”的起点先放进去
        for i in range(min(m,k)):
            heapq.heappush(heap, (nums1[i] + nums2[0],i,0))

        #put the result in heap:
        while heap and len(res) < k:
            cur_sum,i,j = heapq.heappop(heap)
            res.append([nums1[i],nums2[j]])

            if j+1 < n:
                new_sum = nums1[i] + nums2[j+1]
                heapq.heappush(heap, (new_sum,i,j+1))

        return res
