'''
Given an integer n, find all integers s < n such that
s can be expressed as the sum of two squares
s = a^2 + b^2
in exactly two distinct unordered ways, where a and b are non-negative integers and (a, b) and (b, a) 
are considered the same representation.
example: 50 = 1^2 + 7^2 = 5^2 + 5^2
要求找到小于n的所有满足条件的数，1 <= n < 2^31 - 1
'''

'''
input:
output:

'''
import math
from collections import defaultdict
from typing import List

def sums_of_two_squares_exactly_two_ways(n: int) -> List[int]:
    """
    Return all s < n such that s = a^2 + b^2 in exactly two distinct unordered ways,
    where a, b are non-negative integers and (a,b) and (b,a) are considered the same.
    """
    if n <= 1:
        return []

    m = math.isqrt(n - 1)  # max possible a (and b) such that a^2 < n
    count = defaultdict(int)  # sum -> number of (a,b) pairs with a<=b

    for a in range(m + 1):
        a2 = a * a
        max_b = math.isqrt(n - 1 - a2)  # ensure a^2 + b^2 < n
        for b in range(a, max_b + 1):   # b starts at a to avoid counting (b,a)
            s = a2 + b * b
            count[s] += 1

    res = [s for s, c in count.items() if c == 2]
    res.sort()
    return res


# quick test
print(sums_of_two_squares_exactly_two_ways(60))