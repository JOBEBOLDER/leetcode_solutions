class Solution:
    '''
    understand:
    input: arrays List
    output: list:

    logic:
    for each nums[i] find out how many numbers in the array are smaller than it. 

    plan:
    hashtable to store each element index,key:nums[i],value: the index
    sort the array,
    output: calcualte how many element that they are in front of the nums[i],

	•	时间复杂度： ❗O(n log n)（排序的代价）
	•	空间复杂度： ✅O(n)（哈希表 + 结果数组）
    
    '''
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #base case :
        if not nums:
            return []

        sort_array = sorted(nums)

        hash_table = {}

        #only record the first appearance digit
        for i in range(len(sort_array)):
            if sort_array[i] not in hash_table:
                hash_table[sort_array[i]] = i
        
        #traverse the nums again and get the value from the hashtable and reflect to the res:
        res = [hash_table[num] for num in nums]

        return res