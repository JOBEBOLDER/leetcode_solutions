class Solution:
    def maximumSwap(self, num: int) -> int:
        #we only need to iterate the num once
        #time:o1#space:O1

        #inorder to rearrange the num,we need to convert the num to string
        digits = str(num)
        max_index = len(digits) - 1

        p = q = -1

        for i in range(len(digits) - 2, -1,-1):
            if digits[i] > digits[max_index]:
                max_index = i#update the index max_index
            elif digits[i] < digits[max_index]:
                p,q = i,max_index
        
        if p == -1:
            return num

        d_list = list(digits)

        d_list[p],d_list[q] = d_list[q],d_list[p]

        return int("".join(d_list))



