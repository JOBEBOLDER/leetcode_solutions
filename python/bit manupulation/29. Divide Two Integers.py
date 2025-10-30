class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #极端case，如果最大除以最小，返回2**31 - 1
        if dividend == -2**31 and divisor == -1: return 2**31 - 1
        s = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b, q = abs(dividend), abs(divisor), 0
        #t = 当前要尝试减掉的数（初始是1倍的除数）
        #k = 对应的倍数（初始是1）
        while a >= b:
            t, k = b, 1
            #t <<= 1 相当于 t = t × 2
            #k <<= 1 相当于 k = k × 2
            while a >= t << 1:
                t <<= 1
                k <<= 1
            #a 把能减的倍数都减掉，q记录商，然后一次叠加
            a -= t; q += k
        return s * q


'''
第一轮：
a = 48
找到：t = 40, k = 8
执行：a = 48 - 40 = 8
     q = 0 + 8 = 8

第二轮：
a = 8（剩余）
找到：t = 5, k = 1
执行：a = 8 - 5 = 3
     q = 8 + 1 = 9  ← 累加！

第三轮：
a = 3 < 5，退出
最终商 = 9



'''