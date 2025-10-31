class Solution:
    '''
        understand:
        - given nums,
        constrains: only positive, with dup elements

        output:
        max sum score:int

        sliding window, while moving the pointer and keep track of the max sum at the same time
        when shrink the window? when the window contain dup,
        用滑动窗口 + 哈希集合(set)就能“在当前窗口检测是否出现过”。思路是：右指针往右扩；如果新来的 nums[right] 已经在窗口里（in seen），就不断从左边缩小窗口，直到把这个重复值移出为止；同时维护窗口内元素和。
        #time：On
        #space:On
        
        '''
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res=0
        cur_sum = 0
        left = 0
        seen = set()


        for right,x in enumerate(nums):
            #if the element already seen
            #要用while，因为while代表可能连续的dup
            while x in seen:
                #哈希也要remove
                seen.remove(nums[left])
                cur_sum -= nums[left]    
                left += 1
                
            #if the element haven't been seen
            seen.add(x)
            cur_sum += x
            #在最后更新是因为，either seen or unseen,在最后检查都是最保险的
            res=max(cur_sum,res)

        return res





