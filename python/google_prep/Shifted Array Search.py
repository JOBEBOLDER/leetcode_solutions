'''
Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don't have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.

Example:

input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr
Constraints:

[time limit] 5000ms
[input] array.integer arr
[input] integer num
[output] integer
'''

'''
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the



'''
from typing import List

def shifted_arr_search(shiftArr: List[int], num: int) -> int:
    left = 0
    right = len(shiftArr) - 1

    while left <= right:
        mid = left + (right -  left) // 2
        if shiftArr[mid] == num:
            return mid

        if shiftArr[left] <= shiftArr[mid]:
            if shiftArr[left] <= num < shiftArr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if shiftArr[mid] <= num <shiftArr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

            


