class Solution:
    #binary search
    #condition: find: spell * postions >= success
    # = potions = success/ spell(ceil)向上取整
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 对药水数组排序，不要对咒语数组排序
        #首先计算 7/5，结果是浮点数 1.4
        #然后 math.ceil(1.4) 向上取整为 2
        potions.sort()
        res = []
        
        for spell in spells:
            min_potion = math.ceil(success / spell)
            index = bisect_left(potions, min_potion)
            successful_count = len(potions) - index
            res.append(successful_count)
            
        return res

