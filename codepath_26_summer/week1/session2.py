'''
Write a function transpose() that accepts a 
2D integer array matrix and returns the transpose of matrix. 
The transpose of a matrix is the matrix flipped over its main diagonal, 
swapping the rows and columns.

'''

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    res = [[0] * rows for _ in range(cols)]

    for row in range(rows):
        for col in range(cols):
            res[col][row] = matrix[row][col]
    return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))

'''
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until 
our problem is solved or the pointers reach the opposite ends of the list.

'''

def reverse_list(lst):return lst[::-1]
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

# lst[left], lst[right] = lst[right], lst[left]

'''
Write a function remove_dupes() that accepts a sorted array items, 
and removes the duplicates in-place such that each element appears only once. 
Return the length of the modified array. You may not create another array; 
your implementation must modify the original input array items.


'''

def remove_dupes(items):

    seen = set()

    res = []

    for item in items:

        if item not in seen:

            seen.add(item)

            res.append(item)

    return len(res)

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))


'''
Given an integer array nums, 
write a function sort_by_parity() that moves all the even integers 
to the beginning of the array, followed by all the odd integers.

Return any array that satisfies this condition.
'''
'''
even all are on the left, odd all are on the right
so nums[left] == even -> correct
nums[right] == odd -> correct

only swap when:
nums[left] == odd or nums[right] == even

'''
def sort_by_parity(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1

            right -= 1
    return nums

nums = [3, 1, 2, 4]
print(sort_by_parity(nums))

nums = [0]
print(sort_by_parity(nums))


'''
Christopher Robin is helping Pooh construct the biggest hunny jar possible.

Help him write a function that accepts an integer array heights of length n. 
The height of each element is given by heights[i].

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, heights[i]).

Find two lines that, together with the x-axis, form the container that holds the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

max_honey = max()
most_honey(height)

height = [1, 1]
most_honey(height)


'''



def most_honey(heights):
    left = 0
    right = len(heights) - 1
    res = float('-inf')

    while left < right:
        min_height = min(heights[left],heights[right])
        res = max(min_height * (right - left),res)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return res

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(most_honey(height))

height = [1, 1]
print(most_honey(height))

'''
You are given an array of intervals, where each interval is represented as [start, end].

Write a function merge_intervals(intervals) that merges all overlapping intervals 
and returns a new array of the merged, non-overlapping intervals.

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
'''

def merge_intervals(intervals):
    intervals.sort(key=lambda  x:x[0])
    res = []
    for i in range(1,len(intervals)):

        a,b = intervals[i]
        min_num = min(a,intervals[i-1][0])
        max_num = max(b,intervals[i-1][1])
        res.append([min_num,max_num])
    return res
    
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))


    
    
    


